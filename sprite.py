import pygame as pg
from abc import ABC, abstractmethod


class Sprite(ABC, pg.sprite.Sprite):

    @abstractmethod
    def __init__(self):
        super().__init__()
        self.pos_x = 0
        self.pos_y = 0
        self.image = None
        self.rect = None

    @abstractmethod
    def render(self):
        raise NotImplemented

