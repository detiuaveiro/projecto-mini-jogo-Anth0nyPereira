import pygame as pg

from consts import Consts
from sprite import MoveableSprite


class Point(MoveableSprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(pos_x, pos_y, Consts.SPRITE_POINT, Consts.SPRITE_POINT
                         .get_rect(topleft=(pos_x, pos_y)))

    def scale(self, new_width, new_height):
        pg.transform.scale(self.image, (new_width, new_height))

    def render(self, screen):
        super().render(screen)

    def get_rect(self):
        return self.rect

    def get_pos(self):
        return self.pos_x, self.pos_y

    def set_pos(self, new_pos):
        self.pos_x = new_pos[0]
        self.pos_y = new_pos[1]

    def set_rect(self, new_rect):
        self.rect = new_rect
