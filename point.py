import pygame as pg


class Point(pg.sprite.Sprite):
    def __init__(self, pos_x, pos_y, color, width=3):
        super().__init__()
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.color = color
        self.width = width

        self.image = pg.image.load("design/point.png")

        # create a rect to track the position of the object
        self.rect = self.image.get_rect(topleft=(self.pos_x, self.pos_y))

    def render(self, screen):
        screen.blit(self.image, self.rect)

    def get_rect(self):
        return self.rect