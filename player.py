import pygame as pg


class Player(pg.sprite.Sprite):

    def __init__(self):
        # call the parent class (Sprite) constructor
        super().__init__()

        # create an image of the box
        self.image = pg.image.load("design/playerv1.png")

        # create a rect to track the position of the object
        self.rect = self.image.get_rect(topleft=(1100, 550)) # it's actually left and then top

    def render(self, screen):
        screen.blit(self.image, self.rect)

    def get_rect(self):
        return self.rect
