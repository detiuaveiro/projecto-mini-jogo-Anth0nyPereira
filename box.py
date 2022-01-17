import pygame as pg


class Box(pg.sprite.Sprite):

    def __init__(self, pos_x, pos_y):
        # call the parent class (Sprite) constructor
        super().__init__()

        # store the desired position
        self.pos_x = pos_x
        self.pos_y = pos_y

        # create an image of the box
        self.image = pg.image.load("design/box.png")
        # self.image = pg.transform.scale(self.image, (100, 60))

        # create a rect to track the position of the object
        self.rect = self.image.get_rect(topleft=(self.pos_x, self.pos_y)) # this is basically the position, just a reminder, the box is not being scaled yet

    def clone(self):
        # print("here")
        return Box(self.pos_x, self.pos_y)

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




