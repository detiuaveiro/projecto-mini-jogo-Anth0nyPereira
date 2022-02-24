import pygame as pg
from abc import ABC, abstractmethod

from consts import Consts


class Text(ABC):
    """
    An abstract class used to represent a kind of text that needs to be displayed on screen
    """

    @abstractmethod
    def __init__(self, pos_x, pos_y, msg, font_style, size, color):

        """
        Parameters
        ----------

        pos_x: int
               the first coordinate of the position of the text

        pos_y: int
                the second coordinate of the position of the text

        msg: str
                the message that is going to be displayed

        font_style: str
                the font that will be used
                
        color: str
                the color that will be used
        """

        # initializing attributes
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.msg = msg
        self.font_style = font_style
        self.size = size
        self.color = color

        self.font = pg.font.SysFont(self.font_style, self.size, True, False)
        self.text = self.font.render(self.msg, False, color)

    @abstractmethod
    def render(self):
        raise NotImplemented


class ScoreText(Text):
    """
    A concrete text class used to represent the actual score
    """

    def __init__(self):
        self.score = 0
        super().__init__(1000, 40, f'Score: {self.score}', "arial", 30, "white")

    def render(self, screen):
        screen.blit(self.text, (self.pos_x, self.pos_y))  # the text-position is the position of the top-right corner

    def update(self, screen, points):
        self.set_score(points)
        self.set_text()
        self.render(screen)

    def set_text(self):
        self.msg = f'Score: {self.score}'
        self.text = self.font.render(self.msg, False, self.color)

    def get_score(self):
        return self.score

    def set_score(self, new_score):
        self.score += new_score


class GameOverText(Text):
    """
    A concrete text class used to represent the game over text
    """

    def __init__(self):
        super().__init__(Consts.WIDTH // 2, 100, "GAME OVER", "michroma", 80, "red")

    def render(self, screen):
        screen.blit(self.text, (self.text.get_rect(center=(Consts.WIDTH // 2, 100))))
