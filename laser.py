import math

import pygame as pg


class Laser(pg.sprite.Sprite):

    def __init__(self, color, starting_point, ending_point, width=5):
        super().__init__()
        self.color = color
        self.starting_point = starting_point
        self.ending_point = ending_point
        self.width = width

        # self.center = ((ending_point[0] + starting_point[0])/2, (ending_point[1] + starting_point[1])/2)
        # self.size = math.sqrt(((abs(ending_point[0] - starting_point[0])) ** 2) + ((abs(ending_point[1] - starting_point[1])) ** 2))

        self.image = pg.Surface((1500, 1500))
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect(topleft=(0, 0))
        self.render(self.image)
        self.mask = pg.mask.from_surface(self.image)

    '''
    def __init__(self, screen):
        super().__init__()
        self.image = pg.Surface((1000, 1000))
        self.image.set_colorkey((0, 0, 0))
        self.render(self.image)
        self.rect = self.image.get_rect(topleft=(50, 50))
    '''

    def render(self, screen):
        pg.draw.line(screen, self.color, self.starting_point, self.ending_point, self.width)

    def clone(self):
        return Laser(self.color, self.starting_point, self.ending_point, self.width)

    def set_ending_point(self, new_point):
        self.ending_point = new_point