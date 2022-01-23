import pygame as pg

from pygame.constants import *
from abc import ABC


class Command(ABC):
    def execute(self, player):
        raise NotImplemented


class MoveLeft(Command):
    def __init__(self, screen):
        self.screen = screen

    def execute(self, object):
        self.object = object
        self.move_left()

    def move_left(self):
        # print("move left")
        vector = (-5, 0)
        self.object.get_rect().move_ip(-5, 0)
        # print(self.object.get_pos())
        self.object.set_pos((self.object.get_pos()[0] + vector[0], self.object.get_pos()[1] + vector[1]))
        self.object.get_rect().clamp_ip(self.screen.get_rect())


class MoveRight(Command):
    def __init__(self, screen):
        self.screen = screen

    def execute(self, object):
        self.object = object
        self.move_right()

    def move_right(self):
        # print("move right")
        vector = (5, 0)
        self.object.get_rect().move_ip(5, 0)
        self.object.set_pos((self.object.get_pos()[0] + vector[0], self.object.get_pos()[1] + vector[1]))
        self.object.get_rect().clamp_ip(self.screen.get_rect())


class MoveUp(Command):
    def __init__(self, screen):
        self.screen = screen

    def execute(self, object):
        self.object = object
        self.move_up()

    def move_up(self):
        vector = (0, -5)
        self.object.get_rect().move_ip(0, -5)
        self.object.set_pos((self.object.get_pos()[0] + vector[0], self.object.get_pos()[1] + vector[1]))
        self.object.get_rect().clamp_ip(self.screen.get_rect())


class MoveDown(Command):
    def __init__(self, screen):
        self.screen = screen

    def execute(self, object):
        self.object = object
        self.move_down()

    def move_down(self):
        vector = (0, 5)
        self.object.get_rect().move_ip(0, 5)
        self.object.set_pos((self.object.get_pos()[0] + vector[0], self.object.get_pos()[1] + vector[1]))
        self.object.get_rect().clamp_ip(self.screen.get_rect())


class InputHandler:

    def __init__(self, screen):
        self.screen = screen
        self.command = {K_LEFT: MoveLeft(self.screen), K_RIGHT: MoveRight(self.screen), K_UP: MoveUp(self.screen),
                        K_DOWN: MoveDown(self.screen)}

    def handle_input(self, object):
        if pg.key.get_pressed()[K_LEFT]:
            return self.command[K_LEFT].execute(object)
        elif pg.key.get_pressed()[K_RIGHT]:
            return self.command[K_RIGHT].execute(object)
        elif pg.key.get_pressed()[K_UP]:
            return self.command[K_UP].execute(object)
        elif pg.key.get_pressed()[K_DOWN]:
            return self.command[K_DOWN].execute(object)
