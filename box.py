import pygame as pg

from sprite import Sprite


class Box(Sprite):
    """
       A concrete sprite class that represents a box, which means it is an obstacle, where the player can hide from the entity
       Recurring to Prototype design pattern
    """

    def __init__(self, pos_x, pos_y, image, size):
        """
        Parameters
        ----------

        pos_x: int
               the first coordinate of the position of the box

        pos_y: int
                the second coordinate of the position of the box

        image: pygame.Surface
                the variable that stores the loaded box sprite

        size: tuple
                the size of the box, important for scaling
        """

        super().__init__(pos_x, pos_y, image, image.get_rect(topleft=(pos_x, pos_y)))
        self.size = size
        self.image = pg.transform.smoothscale(self.image, self.size)

    def clone(self):
        return Box(self.pos_x, self.pos_y, self.image, self.size)

    def draw(self, screen):
        self.render(screen)

    def render(self, screen):
        screen.blit(self.image, self.rect)

    def set_x(self, new_x):
        self.pos_x = new_x
        self.set_rect(self.image.get_rect(topleft=(self.pos_x, self.pos_y)))

    def set_y(self, new_y):
        self.pos_y = new_y
        self.set_rect(self.image.get_rect(topleft=(self.pos_x, self.pos_y)))

    def set_pos(self, new_pos):
        self.pos_x = new_pos[0]
        self.pos_y = new_pos[1]
        self.set_rect(self.image.get_rect(topleft=(self.pos_x, self.pos_y)))

    def set_rect(self, new_rect):
        self.rect = new_rect

    def get_rect(self):
        return self.rect
