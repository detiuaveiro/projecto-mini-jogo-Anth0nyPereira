import pygame as pg
import numpy as np

from consts import Consts
from point import Point
from sprite import Sprite
from states import EntityState


def get_random_timestamp():
    """
    Return
    ----------
        --> numpy.int64
    """
    timestamp = np.random.uniform(low=3, high=20, size=(1)).astype(int)[0] * 1000  # return in ms
    # print(timestamp)
    return timestamp


class Entity(Sprite):
    """
        A concrete sprite class used to represent the Entity, which is the enemy of this game basically
        Recurring to Singleton, State and Update Method design patterns

        Attributes
        ----------

        _instance: self
                the entity itself

        Methods
        ----------

        wake_up(self)
            Changes the state of the entity from sleeping to awake

        come_back_to_sleep(self)
            Changes the state of the entity from awake to sleeping

        is_awake(self)
            Checks if the entity state is awake or not

        render(self, screen)
            Renders the entity on screen

        update(self, screen)
            Where the change of the entity state takes place

        Functions
        ----------

        get_instance
            Returns the only existent instance of the entity class
        """

    _instance = None

    @staticmethod
    def get_instance():
        if Entity._instance is None:
            Entity()
        return Entity._instance

    def __init__(self):
        if Entity._instance is not None:
            raise Exception("There's already an instance of Entity")
        else:
            # initializing self.pos_x, self.pos_y, self.image and self.rect
            super().__init__(500, 40, Consts.SPRITE_ENTITY_SLEEPING, Consts.SPRITE_ENTITY_SLEEPING
                             .get_rect(topleft=(500, 40)))

            # load both images
            # self.image is already loaded and created by Sprite class
            self.entity_sleeping = Consts.SPRITE_ENTITY_SLEEPING
            self.entity_awake = Consts.SPRITE_ENTITY_AWAKE

            # initialize state
            self.state = EntityState.SLEEPING

            # time when entity will wake up
            self.entity_timestamp = get_random_timestamp()
            self.entity_previous_timestamp = 0

            # create two points at the eyes position
            self.left_point_coords = self.pos_x + 88, self.pos_y + 100
            self.right_point_coords = self.pos_x + 133, self.pos_y + 100
            self.left_point = Point(self.left_point_coords[0], self.left_point_coords[1])
            self.right_point = Point(self.right_point_coords[0], self.right_point_coords[1])

            Entity._instance = self

    def wake_up(self):
        self.image = self.entity_awake
        self.state = EntityState.AWAKE

    def come_back_to_sleep(self):
        self.image = self.entity_sleeping
        self.state = EntityState.SLEEPING
        self.entity_timestamp = get_random_timestamp()
        self.entity_previous_timestamp = pg.time.get_ticks()

    def is_awake(self):
        if self.state == EntityState.AWAKE:
            return True
        return False

    def render(self, screen):
        screen.blit(self.image, self.rect)

    def update(self, screen):
        # check if entity is going to wake up
        # calculate a new timestamp all the time and check if there is enough time so that the entity can wake up, so
        # if the new timestamp is the same as the one that was generated for the entity, or if they are really close
        timestamp = pg.time.get_ticks() - self.entity_previous_timestamp
        entity_timestamp = self.get_entity_timestamp()
        if not self.is_awake() and (
                timestamp == self.get_entity_timestamp() or abs(timestamp - entity_timestamp) <= 19):
            print("waking up")
            self.wake_up()

        if self.is_awake() and abs(timestamp - entity_timestamp) >= 5000:
            print("coming back to sleep")
            self.come_back_to_sleep()

        self.render(screen)

    def get_entity_timestamp(self):
        return self.entity_timestamp

    def get_left_point_coords(self):
        return self.left_point_coords

    def get_right_point_coords(self):
        return self.right_point_coords
