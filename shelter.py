import pygame as pg

from consts import Consts
from point import Point
from sprite import Sprite


class Shelter(Sprite):

    def __init__(self):
        super().__init__(1000, 400, Consts.SPRITE_SHELTER, Consts.SPRITE_SHELTER
                         .get_rect(topleft=(1000, 400)))

        # define rectangle where the player should overlap to drop the food
        self._reference_rect = pg.Rect((1050, 480), (40, 40))

    def render(self, screen):
        screen.blit(self.image, self.rect)

        # render the rectangle on second so that it overlaps the shelter sprite
        # pg.draw.rect(screen, "blue", self._reference_rect)

    def update(self, screen):
        self.render(screen)

    @property
    def reference_rect(self):
        return self._reference_rect


