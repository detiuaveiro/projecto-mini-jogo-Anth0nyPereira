import pygame as pg
from pygame import QUIT

from box_spawner import BoxSpawner, get_box_list
from command import InputHandler
from consts import Consts
from entity import Entity
from food_spawner import FoodSpawner, get_food_list
from laser import Laser
from player import Player
from prototype import LaserSpawner
from shelter import Shelter
from text import ScoreText, GameOverText


class GameManager:
    _instance = None

    @staticmethod
    def get_instance():
        if GameManager._instance is None:
            GameManager()
        return GameManager._instance

    def __init__(self):
        if GameManager._instance is not None:
            raise Exception("There's already an instance of Game Manager")
        else:
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

            self.entity_shelter = pg.sprite.Group()
            self.entity_shelter.add(self.entity)
            self.entity_shelter.add(self.shelter)

            # create boxes

            self.box_machine = BoxSpawner(Consts.ALL_QUADRANT, self.entity_shelter)
            self.box_machine.create_all_boxes()

            # create food
            self.food_machine = FoodSpawner(Consts.FIRST_QUADRANT, self.entity_shelter)
            self.food_machine2 = FoodSpawner(Consts.SECOND_QUADRANT, self.entity_shelter)
            self.food_machine3 = FoodSpawner(Consts.THIRD_QUADRANT, self.entity_shelter)
            self.food_machine4 = FoodSpawner(Consts.FOURTH_QUADRANT, self.entity_shelter)

            # experiment to create a laser spawner
            self.laser_left = Laser("red", self.entity.get_left_point_coords(), self.player.ref_point.get_pos())
            self.laser_right = Laser("red", self.entity.get_right_point_coords(), self.player.ref_point.get_pos())
            self.laser_spawner = LaserSpawner()

            # initialize texts, both ScoreText and GameOverText
            self.score_text = ScoreText()
            self.game_over_text = GameOverText()
            GameManager._instance = self

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

                self.food_machine.update(self.screen)
                self.food_machine2.update(self.screen)
                self.food_machine3.update(self.screen)
                self.food_machine4.update(self.screen)

                self.box_machine.update(self.screen)

                self.shelter.render(self.screen)
                self.player.render(self.screen)

                self.laser_left.set_ending_point(self.player.ref_point.get_pos())
                self.laser_right.set_ending_point(self.player.ref_point.get_pos())
                laser_left = self.laser_spawner.spawn_laser(self.laser_left)
                laser_right = self.laser_spawner.spawn_laser(self.laser_right)

                laser_left.render(self.screen)
                laser_right.render(self.screen)
                hit_left = laser_left.check_collisions(get_box_list())
                hit_right = laser_right.check_collisions(get_box_list())

                # collision with food test
                self.player.update(self.screen, get_food_list(), self.shelter, self.score_text)

                # collisions algorithm
                if self.entity.is_awake() and hit_left and hit_right:
                    print("Game Over")
                    game_over = True

                # pg.draw.rect(self.screen, "red", self.box.get_rect())
                pg.display.flip()
                pg.display.update()

                # call inputHandler
                InputHandler(self.screen).handle_input(self.player, get_box_list())
                # InputHandler(self.screen).handle_input(self.player.ref_point)
