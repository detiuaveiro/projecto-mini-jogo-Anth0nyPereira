import pygame as pg
import numpy as np

from point import Point
from sprite import Sprite
from states import EntityState


def get_random_timestamp():
    timestamp = np.random.uniform(low=3, high=20, size=(1)).astype(int)[0] * 1000  # return in ms
    print(timestamp)
    return timestamp


class Entity(Sprite):
    def __init__(self):

        # initializing self.pos_x, self.pos_y, self.image and self.rect
        super().__init__(500, 40, pg.image.load("design/entity_sleepingv1.png"), pg.image.load("design/entity_sleepingv1.png")
                         .get_rect(topleft=(500, 40)))

        # load both images
        # self.image is already loaded and created by Sprite class
        self.entity_sleeping = pg.image.load("design/entity_sleepingv1.png")
        self.entity_awake = pg.image.load("design/entity_awakev1.png")

        # initialize state
        self.state = EntityState.SLEEPING

        # time when entity will wake up
        self.entity_timestamp = get_random_timestamp()
        # print(self.entity_timestamp)
        self.entity_previous_timestamp = 0

        # create two points at the eyes position
        self.left_point_coords = self.pos_x + 88, self.pos_y + 100
        self.right_point_coords = self.pos_x + 133, self.pos_y + 100
        self.left_point = Point(self.left_point_coords[0], self.left_point_coords[1])
        self.right_point = Point(self.right_point_coords[0], self.right_point_coords[1])

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
        self.left_point.render(screen)
        self.right_point.render(screen)

    def update(self, screen):
        # check if entity is going to wake up
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
