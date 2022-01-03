import pygame as pg


class Box(pg.sprite.Sprite):

    def __init__(self):
        # call the parent class (Sprite) constructor
        super().__init__()

        # create an image of the box
        self.image = pg.image.load("design/box.png")
        self.image = pg.transform.scale(self.image, (100, 50))

        # create a rect to track the position of the object
        self.rect = self.image.get_rect(topleft=(800, 500))

    def render(self, screen):
        screen.blit(self.image, self.rect)
