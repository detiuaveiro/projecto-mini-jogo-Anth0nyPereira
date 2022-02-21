import pygame as pg


class Shelter(pg.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pg.image.load("design/shelter.png")
        self.rect = self.image.get_rect(topleft=(1000, 400))

    def render(self, screen):
        screen.blit(self.image, self.rect)


