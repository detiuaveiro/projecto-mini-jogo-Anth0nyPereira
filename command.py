import pygame as pg

from pygame.constants import *
from abc import ABC


class Command(ABC):
    def execute(self, player):
        raise NotImplemented

    def undo(self, player):
        raise NotImplemented


class MoveLeft(Command):
    def __init__(self, screen):
        self.screen = screen

    def execute(self, player):
        player.move_left(self.screen)


class MoveRight(Command):
    def __init__(self, screen):
        self.screen = screen

    def execute(self, player):
        player.move_right(self.screen)


class MoveUp(Command):
    def __init__(self, screen):
        self.screen = screen

    def execute(self, player):
        player.move_up(self.screen)


class MoveDown(Command):
    def __init__(self, screen):
        self.screen = screen

    def execute(self, player):
        player.move_down(self.screen)


class InputHandler:

    def __init__(self, screen):
        self.screen = screen
        self.command = {K_LEFT: MoveLeft(self.screen), K_RIGHT: MoveRight(self.screen), K_UP: MoveUp(self.screen),
                        K_DOWN: MoveDown(self.screen)}

    def handle_input(self, player):

        if pg.key.get_pressed()[K_LEFT]:
            self.command[K_LEFT].execute(player)
        elif pg.key.get_pressed()[K_RIGHT]:
            self.command[K_RIGHT].execute(player)
        if pg.key.get_pressed()[K_UP]:
            self.command[K_UP].execute(player)
        elif pg.key.get_pressed()[K_DOWN]:
            self.command[K_DOWN].execute(player)
