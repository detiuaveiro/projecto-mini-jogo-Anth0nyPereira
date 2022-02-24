import pygame as pg

from consts import Consts
from point import Point
from sprite import MoveableSprite
from states import PlayerState


class Player(MoveableSprite):

    def __init__(self, pos_x, pos_y):

        # initializing self.pos_x, self.pos_y, self.image and self.rect
        super().__init__(pos_x, pos_y, pg.image.load("design/playerv1.png"),
                         pg.image.load("design/playerv1.png")
                         .get_rect(topleft=(pos_x, pos_y)))

        # create a point to use it for the collision algorithm
        self.ref_point = Point(self.pos_x + 15, self.pos_y + 15)

        # initialize state of player
        self.state = PlayerState.WITHOUT_FOOD

        # initialize pointer to picked food
        self.food = None

    def update(self, screen, food_list, shelter, score):
        food_hit = pg.sprite.spritecollideany(self, food_list)
        shelter_hit = self.get_rect().colliderect(shelter.reference_rect)

        if self.state == PlayerState.WITHOUT_FOOD and food_hit:
            self.food = food_hit
            self.state = PlayerState.WITH_FOOD
            self.image = pg.image.load("design/playerwithfood.png")
            food_hit.kill()
            pg.display.update()

        if self.state == PlayerState.WITH_FOOD is not None and shelter_hit:

            # call update_score event
            ev = pg.event.Event(Consts.CUSTOM_GAME_EVENT, {"name": Consts.UPDATE_SCORE, "points": self.food.get_score()})
            pg.event.post(ev)
            self.food = None
            self.state = PlayerState.WITHOUT_FOOD
            self.image = pg.image.load("design/playerv1.png")
            pg.display.update()

        self.render(screen)

    def render(self, screen):
        super().render(screen)
        self.ref_point.render(screen)

