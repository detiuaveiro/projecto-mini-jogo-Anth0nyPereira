import pygame as pg
import numpy as np

from point import Point


def get_random_timestamp():
    return np.random.uniform(low=3, high=20, size=(1)).astype(int)[0] * 1000  # return in ms


class Entity:
    def __init__(self):
        self.pos_x = 500
        self.pos_y = 40

        # load both images
        self.entity_sleeping = pg.image.load("design/entity_sleepingv1.png")
        self.entity_awake = pg.image.load("design/entity_awakev1.png")
        self.actual_entity = self.entity_sleeping

        # time when entity will wake up
        self.entity_timestamp = get_random_timestamp()
        print(self.entity_timestamp)
        self.entity_previous_timestamp = 0

        # create two points at the eyes position
        self.left_point_coords = (self.pos_x + 88, self.pos_y + 100)
        self.right_point_coords = (self.pos_x + 133, self.pos_y + 100)
        self.left_point = Point(self.left_point_coords)
        self.right_point = Point(self.right_point_coords)

    def wake_up(self):
        self.actual_entity = self.entity_awake

    def come_back_to_sleep(self):
        self.actual_entity = self.entity_sleeping
        self.entity_timestamp = get_random_timestamp()
        self.entity_previous_timestamp = pg.time.get_ticks()
        print(self.entity_timestamp)

    def is_awake(self):
        if self.actual_entity == self.entity_awake:
            return True
        return False

    def render(self, screen):
        screen.blit(self.actual_entity, (self.pos_x, self.pos_y))
        self.left_point.render(screen)
        self.right_point.render(screen)

    def get_entity_timestamp(self):
        return self.entity_timestamp

    def get_left_point_coords(self):
        return self.left_point_coords

    def get_right_point_coords(self):
        return self.right_point_coords
