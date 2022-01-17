import pygame as pg


class Point:
    def __init__(self, pos_x, pos_y, color, width=3):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.color = color
        self.width = width

    def render(self, screen):
        pg.draw.circle(screen, self.color, (self.pos_x, self.pos_y), self.width)
