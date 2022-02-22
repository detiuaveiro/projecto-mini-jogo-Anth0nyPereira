import pygame as pg


class Text:

    def __init__(self, msg):
        self.font = pg.font.SysFont('michroma', 80, True, False)
        self.msg = msg
        '''
            game_over_msg = "Game Over"
            game_over_txt = font.render(game_over_msg, False, 'red')
        '''

    def render(self):
        raise NotImplemented
