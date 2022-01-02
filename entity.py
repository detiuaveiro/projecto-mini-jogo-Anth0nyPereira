import pygame as pg


class Entity:
    def __init__(self):
        self.pos_x = 500
        self.pos_y = 40

        # load both images
        self.entity_sleeping = pg.image.load("design/entity_sleepingv1.png")
        self.entity_awake = pg.image.load("design/entity_awakev1.png")
        self.actual_entity = self.entity_sleeping

    def render(self, screen):
        screen.blit(self.actual_entity, (self.pos_x, self.pos_y))
