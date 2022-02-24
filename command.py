import pygame as pg

from pygame.constants import *
from abc import ABC


class Command(ABC):
    """
    A base class for the Command design pattern
    """

    def execute(self):
        raise NotImplemented

    def undo(self):
        raise NotImplemented


class MoveLeft(Command):
    """
    A concrete command class used to make the action of moving to the left

    Methods
    ----------

    execute(self, player, obstacles)
        Moves the player to the left, if there is no collision between obstacles

    def undo(self, player):
        Moves to the opposite direction, to the right
    """

    def __init__(self, screen):
        """
        Parameters
        ----------

        screen: pygame.Surface
            the screen where everything in-game is rendered

        """
        self.screen = screen

    def execute(self, player, obstacles):
        player.move_left(self.screen)
        obstacles_hit = pg.sprite.spritecollide(player, obstacles, False)
        if len(obstacles_hit) > 0:
            self.undo(player)
        else:
            player.ref_point.move_left(self.screen)

    def undo(self, player):
        player.move_right(self.screen)


class MoveRight(Command):
    """
        A concrete command class used to make the action of moving to the right

        Methods
        ----------

        execute(self, player, obstacles)
            Moves the player to the right, if there is no collision between obstacles

        def undo(self, player):
            Moves to the opposite direction, to the left
        """

    def __init__(self, screen):
        """
        Parameters
        ----------

        screen: pygame.Surface
            the screen where everything in-game is rendered

        """
        self.screen = screen

    def execute(self, player, obstacles):
        player.move_right(self.screen)
        obstacles_hit = pg.sprite.spritecollide(player, obstacles, False)
        if len(obstacles_hit) > 0:
            self.undo(player)
        else:
            player.ref_point.move_right(self.screen)

    def undo(self, player):
        player.move_left(self.screen)


class MoveUp(Command):
    """
        A concrete command class used to make the action of moving up

        Methods
        ----------

        execute(self, player, obstacles)
            Moves up the player, if there is no collision between obstacles

        def undo(self, player):
            Moves to the opposite direction, down
        """

    def __init__(self, screen):
        """
        Parameters
        ----------

        screen: pygame.Surface
            the screen where everything in-game is rendered

        """
        self.screen = screen

    def execute(self, player, obstacles):
        player.move_up(self.screen)
        obstacles_hit = pg.sprite.spritecollide(player, obstacles, False)
        if len(obstacles_hit) > 0:
            self.undo(player)
        else:
            player.ref_point.move_up(self.screen)

    def undo(self, player):
        player.move_down(self.screen)


class MoveDown(Command):
    """
    A concrete command class used to make the action of moving down

    Methods
    ----------

    execute(self, player, obstacles)
        Moves down the player, if there is no collision between obstacles

    def undo(self, player):
        Moves to the opposite direction, up
    """

    def __init__(self, screen):
        """
        Parameters
        ----------

        screen: pygame.Surface
            the screen where everything in-game is rendered

        """
        self.screen = screen

    def execute(self, player, obstacles):
        player.move_down(self.screen)
        obstacles_hit = pg.sprite.spritecollide(player, obstacles, False)
        if len(obstacles_hit) > 0:
            self.undo(player)
        else:
            player.ref_point.move_down(self.screen)

    def undo(self, player):
        player.move_up(self.screen)


class InputHandler:
    """
    Class where the input takes place

    Methods
    ----------

    handle_input(self, player, obstacles)
        Moves the player to a specific direction, depending on the input obtained
    """

    def __init__(self, screen):
        """
        Parameters
        ----------

        screen: pygame.Surface
            the screen where everything in-game is rendered

        """
        self.screen = screen
        self.command = {K_LEFT: MoveLeft(self.screen), K_RIGHT: MoveRight(self.screen), K_UP: MoveUp(self.screen),
                        K_DOWN: MoveDown(self.screen)}

    def handle_input(self, player, obstacles):

        if pg.key.get_pressed()[K_LEFT]:
            self.command[K_LEFT].execute(player, obstacles)
        elif pg.key.get_pressed()[K_RIGHT]:
            self.command[K_RIGHT].execute(player, obstacles)
        if pg.key.get_pressed()[K_UP]:
            self.command[K_UP].execute(player, obstacles)
        elif pg.key.get_pressed()[K_DOWN]:
            self.command[K_DOWN].execute(player, obstacles)
