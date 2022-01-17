import pygame as pg


class Point(pg.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.pos_x = pos[0]
        self.pos_y = pos[1]

        self.image = pg.image.load("design/point.png")

        # create a rect to track the position of the object
        self.rect = self.image.get_rect(topleft=(self.pos_x, self.pos_y))

    def render(self, screen):
        screen.blit(self.image, self.rect)

    def get_rect(self):
        return self.rect

    def get_pos(self):
        return self.pos_x, self.pos_y

    def set_pos(self, new_pos):
        self.pos_x = new_pos[0]
        self.pos_y = new_pos[1]

    def set_rect(self, new_rect):
        self.rect = new_rect