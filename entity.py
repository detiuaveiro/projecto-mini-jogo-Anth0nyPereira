import pygame as pg
import numpy as np


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

    def get_entity_timestamp(self):
        return self.entity_timestamp
