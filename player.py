import pygame as pg

from point import Point


class Player(pg.sprite.Sprite):

    def __init__(self, pos_x, pos_y):
        # call the parent class (Sprite) constructor
        super().__init__()

        # initialize parameters
        self.pos_x = pos_x
        self.pos_y = pos_y

        # create an image of the box
        self.image = pg.image.load("design/playerv1.png")

        # create a rect to track the position of the object
        self.rect = self.image.get_rect(topleft=(self.pos_x, self.pos_y)) # it's actually left and then top

        # create a point to use it to the collision algorithm
        self.ref_point = Point(self.pos_x + 15, self.pos_y + 15)

    def render(self, screen):
        screen.blit(self.image, self.rect)
        self.ref_point.render(screen)

    def get_rect(self):
        return self.rect
