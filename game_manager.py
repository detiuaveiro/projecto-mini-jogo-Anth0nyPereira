import pygame as pg
from pygame import QUIT

from box_spawner import BoxSpawner, get_box_list
from command import InputHandler
from consts import Consts
from entity import Entity
from food_spawner import FoodSpawner, get_food_list
from laser import Laser
from observer import GameOverSubject, GameOverObserver
from player import Player
from laser_spawner import LaserSpawner
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
            pg.display.set_caption("DELIVER ME :(")
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

            # initialize pointers to hit_left and hit_right
            self.hit_left = None
            self.hit_right = None

            # initialize texts, both ScoreText and GameOverText
            self.score_text = ScoreText()
            self.game_over_text = GameOverText()

            self.game_over = Consts.GAME_OVER

            # observer experiment
            # for observer design pattern purpose
            self.entity_notify = GameOverSubject()
            self.entity_notify.add_observer(GameOverObserver())

            GameManager._instance = self

    def update(self):
        self.shelter.update(self.screen)
        # collision with food test
        self.player.update(self.screen, get_food_list(), self.shelter, self.score_text)

        self.entity.update(self.screen)
        self.food_machine.update(self.screen)
        self.food_machine2.update(self.screen)
        self.food_machine3.update(self.screen)
        self.food_machine4.update(self.screen)
        self.box_machine.update(self.screen)
        self.laser_left.update(self.screen, self.player)
        self.laser_right.update(self.screen, self.player)

        self.entity_notify.update(self.hit_left, self.hit_right)

    def run(self):
        running = True
        while running:
            self.clock.tick(60)
            self.screen.fill("black")
            if self.game_over:
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

                    # custom events
                    if event.type == Consts.CUSTOM_GAME_EVENT:
                        if event.name == Consts.UPDATE_SCORE:
                            self.score_text.update(self.screen, event.points)
                        '''
                        elif event.name == Consts.SET_GAME_OVER:
                            print("Game Over")
                            game_over = True
                        '''

                self.screen.blit(self.background, (0, 0))
                self.score_text.render(self.screen)

                self.laser_left = self.laser_spawner.spawn_laser(self.laser_left)
                self.laser_right = self.laser_spawner.spawn_laser(self.laser_right)

                self.hit_left = self.laser_left.check_collisions(get_box_list())
                self.hit_right = self.laser_right.check_collisions(get_box_list())

                self.update()

                self.game_over = Consts.GAME_OVER

                # pg.draw.rect(self.screen, "red", self.box.get_rect())
                pg.display.flip()
                pg.display.update()

                # call inputHandler
                InputHandler(self.screen).handle_input(self.player, get_box_list())
                # InputHandler(self.screen).handle_input(self.player.ref_point)
