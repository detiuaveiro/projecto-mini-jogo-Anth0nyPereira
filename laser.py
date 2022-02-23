import math

import pygame as pg
from pygame import Vector2


class Laser(pg.sprite.Sprite):

    def __init__(self, color, starting_point, ending_point, width=5):
        super().__init__()
        self.color = color
        self.starting_point = starting_point
        self.ending_point = ending_point
        self.width = width

        # self.center = ((ending_point[0] + starting_point[0])/2, (ending_point[1] + starting_point[1])/2)
        # self.size = math.sqrt(((abs(ending_point[0] - starting_point[0])) ** 2) + ((abs(ending_point[1] - starting_point[1])) ** 2))
        '''
        self.image = pg.Surface((1500, 1500))
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect(topleft=(0, 0))
        self.render(self.image)
        self.mask = pg.mask.from_surface(self.image)
        '''

        self.vector = Vector2(self.ending_point[0] - self.starting_point[0],
                              self.ending_point[1] - self.starting_point[1])
        self.angle = self.vector.angle_to(Vector2(1, 0))
        self.m = math.tan(self.angle)
        self.b = starting_point[1] - self.m * starting_point[0]
        self.positions = []
        x = min(starting_point[0], ending_point[0])
        while x < max(starting_point[0], ending_point[0]):
            y = self.m * x + self.b
            self.positions.append((x, y))
            x += 1
        # print(self.positions)

    '''
    def __init__(self, screen):
        super().__init__()
        self.image = pg.Surface((1000, 1000))
        self.image.set_colorkey((0, 0, 0))
        self.render(self.image)
        self.rect = self.image.get_rect(topleft=(50, 50))
    '''

    def check_collisions(self, box_list):
        # checks if there are points from the line given by the starting and ending points
        # inside the specified object aka box, the output gives the start and end points from the box that belong to the
        # line
        '''
        if box.rect.clipline((self.starting_point, self.ending_point)) != ():
            return True
        return False
        '''
        # print(f'Box get rect: {box.get_rect()}')

        for coord in self.positions:
            for box in box_list:
                if pg.Rect.collidepoint(box.get_rect(), coord):
                    # print(coord)
                    return True
        return False

    def render(self, screen):
        pg.draw.line(screen, self.color, self.starting_point, self.ending_point, self.width)

    def clone(self):
        return Laser(self.color, self.starting_point, self.ending_point, self.width)

    def set_ending_point(self, new_point):
        self.ending_point = new_point
