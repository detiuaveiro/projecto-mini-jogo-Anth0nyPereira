import pygame as pg

from point import Point


class Shelter(pg.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pg.image.load("design/shelter.png")
        self.pos_x = 1000
        self.pos_y = 400
        self.rect = self.image.get_rect(topleft=(1000, 400))

        # define rectangle where the player should overlap to drop the food
        self._reference_rect = pg.Rect((1050, 480), (40, 40))

    def render(self, screen):
        screen.blit(self.image, self.rect)

        # render the rectangle on second so that it overlaps the shelter sprite
        pg.draw.rect(screen, "blue", self._reference_rect)

    @property
    def reference_rect(self):
        return self._reference_rect


