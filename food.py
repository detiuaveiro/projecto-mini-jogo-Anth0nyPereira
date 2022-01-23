import pygame as pg


class Food(pg.sprite.Sprite):

    def __init__(self, screen):
        super().__init__()
        self.image = pg.image.load("design/naco.png")
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect(topleft=(500, 500))

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
