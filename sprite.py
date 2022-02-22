import pygame as pg
from abc import ABC, abstractmethod


class Sprite(ABC, pg.sprite.Sprite):

    @abstractmethod
    def __init__(self, pos_x, pos_y, image, rect):
        super().__init__()
        self.pos_x = pos_x
        self.pos_y = pos_y

        # create variable that will load the sprite itself
        self.image = image

        # create a rect to track the position of the object
        self.rect = rect

    @abstractmethod
    def render(self):
        raise NotImplemented

