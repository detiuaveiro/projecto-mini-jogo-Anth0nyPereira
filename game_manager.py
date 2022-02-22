import pygame as pg
from pygame import QUIT

from box import Box
from command import InputHandler
from consts import Consts
from entity import Entity
from flyweight import FoodSpawner
from laser import Laser
from player import Player
from prototype import LaserSpawner
from shelter import Shelter
from text import ScoreText, GameOverText


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
        self.box_list.add(self.entity)

        self.all_obstacles_list = pg.sprite.Group()
        self.all_obstacles_list.add(self.box)
        self.all_obstacles_list.add(self.entity)
        self.all_obstacles_list.add(self.shelter)

        # create food
        self.food_machine = FoodSpawner(Consts.FIRST_QUADRANT)
        self.food_machine2 = FoodSpawner(Consts.SECOND_QUADRANT)
        self.food_machine3 = FoodSpawner(Consts.THIRD_QUADRANT)
        self.food_machine4 = FoodSpawner(Consts.FOURTH_QUADRANT)

        # experiment to create a box spawner
        # box_spawner = BoxSpawner()
        # box2 = box_spawner.spawn_box(box)
        # print(f'{box2.pos_x} - {box2.pos_y}')
        # box2.set_pos(400, 526)

        # experiment to create a laser spawner
        self.laser_left = Laser("red", self.entity.get_left_point_coords(), self.player.ref_point.get_pos())
        self.laser_right = Laser("red", self.entity.get_right_point_coords(), self.player.ref_point.get_pos())
        self.laser_spawner = LaserSpawner()

        # initialize texts, both ScoreText and GameOverText
        self.score_text = ScoreText()
        self.game_over_text = GameOverText()

    def run(self):
        running = True
        game_over = False
        while running:
            self.clock.tick(60)
            self.screen.fill("black")
            if game_over:
                self.game_over_text.render(self.screen)

                for event in pg.event.get():
                    if event.type == QUIT:
                        pg.quit()
                        exit()
                pg.display.update()
            else:

                for event in pg.event.get():
                    if event.type == QUIT:
                        pg.quit()
                        exit()

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

                self.screen.blit(self.background, (0, 0))
                self.score_text.render(self.screen)
                self.box_list.draw(self.screen)
                '''
                self.entity.render(self.screen)  # experiment to draw the entity
                '''
                self.shelter.render(self.screen)
                self.player.render(self.screen)

                self.food_machine.update(self.screen, self.all_obstacles_list)
                self.food_machine2.update(self.screen, self.all_obstacles_list)
                self.food_machine3.update(self.screen, self.all_obstacles_list)
                self.food_machine4.update(self.screen, self.all_obstacles_list)

                self.laser_left.set_ending_point(self.player.ref_point.get_pos())
                self.laser_right.set_ending_point(self.player.ref_point.get_pos())
                laser_left = self.laser_spawner.spawn_laser(self.laser_left)
                laser_right = self.laser_spawner.spawn_laser(self.laser_right)

                laser_left.render(self.screen)
                laser_right.render(self.screen)
                hit_left = laser_left.check_collisions(self.box)
                hit_right = laser_right.check_collisions(self.box)

                # collision with food test
                self.player.update(self.screen, self.food_machine.get_food_list(), self.shelter, self.score_text)
                self.player.update(self.screen, self.food_machine2.get_food_list(), self.shelter, self.score_text)
                self.player.update(self.screen, self.food_machine3.get_food_list(), self.shelter, self.score_text)
                self.player.update(self.screen, self.food_machine4.get_food_list(), self.shelter, self.score_text)

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
