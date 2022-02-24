import pygame as pg
from abc import ABC, abstractmethod


class Sprite(ABC, pg.sprite.Sprite):

    @abstractmethod
    def __init__(self, pos_x, pos_y, image, rect):
        super().__init__()
        self.pos_x = pos_x
        self.pos_y = pos_y

        # create variable that will load the sprite itself
        self.image = image

        # create a rect to track the position of the object
        self.rect = rect

    @abstractmethod
    def render(self):
        raise NotImplemented

    def get_rect(self):
        return self.rect

    def get_pos(self):
        return self.pos_x, self.pos_y

    def set_pos(self, new_pos):
        self.pos_x = new_pos[0]
        self.pos_y = new_pos[1]
        # self.set_rect(self.image.get_rect(topleft=(self.pos_x, self.pos_y)))
        # self.ref_point.set_rect(self.image.get_rect(topleft=(self.pos_x, self.pos_y)))

    def set_rect(self, new_rect):
        self.rect = new_rect


class MoveableSprite(Sprite):

    def __init__(self, pos_x, pos_y, image, rect):
        # call the abstract parent class (Sprite) constructor
        # initializing self.pos_x, self.pos_y, self.image and self.rect
        super().__init__(pos_x, pos_y, image, image.get_rect(topleft=(pos_x, pos_y)))

    def move_left(self, screen):
        vector = (-5, 0)
        self.get_rect().move_ip(-5, 0)
        # print(self.object.get_pos())
        self.set_pos((self.get_pos()[0] + vector[0], self.get_pos()[1] + vector[1]))
        self.get_rect().clamp_ip(screen.get_rect())

    def move_right(self, screen):
        vector = (5, 0)
        self.get_rect().move_ip(5, 0)
        self.set_pos((self.get_pos()[0] + vector[0], self.get_pos()[1] + vector[1]))
        self.get_rect().clamp_ip(screen.get_rect())

    def move_up(self, screen):
        vector = (0, -5)
        self.get_rect().move_ip(0, -5)
        self.set_pos((self.get_pos()[0] + vector[0], self.get_pos()[1] + vector[1]))
        self.get_rect().clamp_ip(screen.get_rect())

    def move_down(self, screen):
        vector = (0, 5)
        self.get_rect().move_ip(0, 5)
        self.set_pos((self.get_pos()[0] + vector[0], self.get_pos()[1] + vector[1]))
        self.get_rect().clamp_ip(screen.get_rect())

    def render(self, screen):
        screen.blit(self.image, self.rect)
