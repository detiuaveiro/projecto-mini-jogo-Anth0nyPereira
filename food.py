import pygame as pg

from sprite import Sprite


class Food(Sprite):

    def __init__(self, pos_x, pos_y, image, score):

        super().__init__(pos_x, pos_y, image, image.get_rect(topleft=(pos_x, pos_y)))

        self.score = score

    def draw(self, screen):
        self.render(screen)

    def render(self, screen):
        screen.blit(self.image, self.rect)

    def clone(self):
        return Food(self.pos_x, self.pos_y, self.image, self.score)

    def set_x(self, new_x):
        self.pos_x = new_x
        self.set_rect(self.image.get_rect(topleft=(self.pos_x, self.pos_y)))

    def set_y(self, new_y):
        self.pos_y = new_y
        self.set_rect(self.image.get_rect(topleft=(self.pos_x, self.pos_y)))

    def set_pos(self, new_pos):
        self.pos_x = new_pos[0]
        self.pos_y = new_pos[1]
        self.set_rect(self.image.get_rect(topleft=(self.pos_x, self.pos_y)))

    def set_rect(self, new_rect):
        self.rect = new_rect

    def get_score(self):
        return self.score

