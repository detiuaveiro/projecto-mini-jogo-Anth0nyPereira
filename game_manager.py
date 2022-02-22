import pygame as pg
from pygame import QUIT

from box import Box
from command import InputHandler
from consts import Consts
from entity import Entity
from food import Food
from laser import Laser
from player import Player
from prototype import LaserSpawner
from shelter import Shelter


class GameManager:

    def __init__(self):
        self.screen = pg.display.set_mode((Consts.WIDTH, Consts.HEIGHT))
        pg.display.set_caption("game made with pygame")
        self.clock = pg.time.Clock()

        # set background
        self.background = pg.image.load("design/background.png")
        self.background = pg.transform.scale(self.background, (Consts.WIDTH, Consts.HEIGHT))

        # create player
        self.player = Player(1100, 550)

        # create entity
        self.entity = Entity()

        # create shelter
        self.shelter = Shelter()

        # create box to hide the player
        self.box_list = pg.sprite.Group()
        self.box = Box(600, 526)
        # box = Box(screen, 1000, 526)
        self.box_list.add(self.box)

        # create food
        food = Food(500, 500)
        self.food_lst = pg.sprite.Group()
        self.food_lst.add(food)

        # experiment to create a box spawner
        # box_spawner = BoxSpawner()
        # box2 = box_spawner.spawn_box(box)
        # print(f'{box2.pos_x} - {box2.pos_y}')
        # box2.set_pos(400, 526)

        # experiment to create a laser spawner
        self.laser_left = Laser("red", self.entity.get_left_point_coords(), self.player.ref_point.get_pos())
        self.laser_right = Laser("red", self.entity.get_right_point_coords(), self.player.ref_point.get_pos())
        self.laser_spawner = LaserSpawner()

        self.font = pg.font.SysFont('arial', 30, True, False)
        self.score = 0

    def run(self):
        running = True
        game_over = False
        while running:
            self.clock.tick(60)
            self.screen.fill("black")
            if game_over:
                # print(pg.font.get_fonts())
                font = pg.font.SysFont('michroma', 80, True, False)

                self.screen.blit(game_over_txt, (game_over_txt.get_rect(center=(Consts.WIDTH // 2, 100))))
                for event in pg.event.get():
                    if event.type == QUIT:
                        pg.quit()
                        exit()
                pg.display.update()
            else:
                message = f'Score: {self.score}'
                final_text = self.font.render(message, False, 'white')

                for event in pg.event.get():
                    if event.type == QUIT:
                        pg.quit()
                        exit()

                '''
                if pg.key.get_pressed()[K_LEFT]:
                    player.get_rect().move_ip(-1, 0)
                    player.get_rect().clamp_ip(screen.get_rect())
                if pg.key.get_pressed()[K_RIGHT]:
                    player.get_rect().move_ip(1, 0)
                    player.get_rect().clamp_ip(screen.get_rect())

                '''

                # check if entity is going to wake up
                timestamp = pg.time.get_ticks() - self.entity.entity_previous_timestamp
                entity_timestamp = self.entity.get_entity_timestamp()
                if not self.entity.is_awake() and (
                        timestamp == self.entity.get_entity_timestamp() or abs(timestamp - entity_timestamp) <= 15):
                    print("waking up")
                    self.entity.wake_up()

                if self.entity.is_awake() and abs(timestamp - entity_timestamp) >= 5000:
                    print("coming back to sleep")
                    self.entity.come_back_to_sleep()
                '''
                # check if player collides with box
                box_hit_lst = pg.sprite.spritecollide(player, box_list, False)
                if entity.is_awake() and not box_hit_lst:  # if list is empty, no collision, so game over
                    print("Game Over")
                    game_over = True
                '''

                self.screen.blit(self.background, (0, 0))
                self.screen.blit(final_text, (1000, 40))  # the text-position is the position of the top-right corner
                self.entity.render(self.screen)  # experiment to draw the entity
                self.shelter.render(self.screen)
                self.player.render(self.screen)

                self.food_lst.draw(self.screen)
                # box.render(screen)
                # box2.render(screen)

                # create laser experiment
                # laser_left = Laser()
                # laser_left = Laser("red", entity.get_left_point_coords(), player.ref_point.get_pos())
                # laser_left.render(screen)

                # laser_right = Laser()
                # laser_right = Laser("red", entity.get_right_point_coords(), player.ref_point.get_pos())
                # laser_right.render(screen)

                self.laser_left.set_ending_point(self.player.ref_point.get_pos())
                self.laser_right.set_ending_point(self.player.ref_point.get_pos())
                laser_left = self.laser_spawner.spawn_laser(self.laser_left)
                laser_right = self.laser_spawner.spawn_laser(self.laser_right)
                '''
                group = pg.sprite.Group([box, laser_left, laser_right])
                group.draw(screen)
                '''
                laser_left.render(self.screen)
                laser_right.render(self.screen)
                self.box_list.draw(self.screen)
                hit_left = laser_left.check_collisions(self.box)
                hit_right = laser_right.check_collisions(self.box)
                # print(hit_left)
                # hit_right = pg.sprite.collide_mask(laser_right, self.box)

                # collision with food test
                self.player.update(self.food_lst, self.shelter)

                # collisions algorithm

                for box in self.box_list:
                    if self.entity.is_awake() and hit_left and hit_right:
                        print("Game Over")
                        game_over = True

                # pg.draw.rect(self.screen, "red", self.box.get_rect())
                pg.display.flip()
                pg.display.update()

                # call inputHandler
                InputHandler(self.screen).handle_input(self.player, self.box_list)
                # InputHandler(self.screen).handle_input(self.player.ref_point)
