import pygame as pg


class Laser:
    def __init__(self, color, starting_point, ending_point, width=3):
        self.color = color
        self.starting_point = starting_point
        self.ending_point = ending_point
        self.width = width

    def render(self, screen):
        pg.draw.line(screen, self.color, self.starting_point, self.ending_point, self.width)
