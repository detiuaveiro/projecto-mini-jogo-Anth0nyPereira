import pygame as pg
from abc import ABC, abstractmethod
from consts import Consts
from text import GameOverText


class Screen(ABC):

    def __init__(self):
        self.screen = pg.display.set_mode((Consts.WIDTH, Consts.HEIGHT))
        pg.display.set_caption("DELIVER ME :(")
        self.screen.fill("black")

    def render(self):
        raise NotImplemented

    @property
    def get_screen(self):
        return self.screen

class MainScreen(Screen):
    def __init__(self):
        super().__init__()
        self.background = pg.image.load("design/background.png")
        self.background = pg.transform.scale(self.background, (Consts.WIDTH, Consts.HEIGHT))

class MainMenu(Screen):


class GameOverScreen(Screen):
    def __init__(self):
        super().__init__()
        self.game_over_text = GameOverText()