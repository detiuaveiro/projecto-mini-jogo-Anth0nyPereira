import pygame as pg

from sprite import Sprite


class Box(Sprite):

    def __init__(self, pos_x, pos_y):
        super().__init__(pos_x, pos_y, pg.image.load("design/box.png"), pg.image.load("design/box.png")
                         .get_rect(topleft=(pos_x, pos_y)))

    def clone(self):
        # print("here")
        return Box(self.pos_x, self.pos_y)

    def draw(self, screen):
        self.render(screen)

    def render(self, screen):
        screen.blit(self.image, self.rect)

    def set_x(self, new_x):
        self.pos_x = new_x
        self.set_rect(self.image.get_rect(topleft=(self.pos_x, self.pos_y)))

    def set_y(self, new_y):
        self.pos_y = new_y
        self.set_rect(self.image.get_rect(topleft=(self.pos_x, self.pos_y)))

    def set_pos(self, new_x, new_y):
        self.pos_x = new_x
        self.pos_y = new_y
        self.set_rect(self.image.get_rect(topleft=(self.pos_x, self.pos_y)))

    def set_rect(self, new_rect):
        self.rect = new_rect

    def get_rect(self):
        return self.rect
