import pygame as pg

from consts import Consts
from point import Point
from sprite import MoveableSprite
from states import PlayerState


class Player(MoveableSprite):
    """
    A concrete moveable sprite class that represents the player itself
    Recurring to State, Subclass Sandbox and Update Method design patterns

    Methods
    ----------

    render(self, screen)
        Draws the player sprite

    update(self, screen, food_list, shelter, score)
        Where the player changes its state when catching food and dropping it in the shelter
        This is also where the event to update the overall score is fired
    """

    def __init__(self, pos_x, pos_y):

        """
        Parameters
        ----------

        pos_x: int
               the first coordinate of the position of the player

        pos_y: int
                the second coordinate of the position of the player

        """

        # initializing self.pos_x, self.pos_y, self.image and self.rect
        super().__init__(pos_x, pos_y, Consts.SPRITE_PLAYER_WITHOUT_FOOD,
                         Consts.SPRITE_PLAYER_WITHOUT_FOOD
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
            self.image = Consts.SPRITE_PLAYER_WITH_FOOD
            food_hit.kill()
            pg.display.update()

        if self.state == PlayerState.WITH_FOOD is not None and shelter_hit:

            # call update_score event
            ev = pg.event.Event(Consts.CUSTOM_GAME_EVENT, {"name": Consts.UPDATE_SCORE, "points": self.food.get_score()})
            pg.event.post(ev)
            self.food = None
            self.state = PlayerState.WITHOUT_FOOD
            self.image = Consts.SPRITE_PLAYER_WITHOUT_FOOD
            pg.display.update()

        self.render(screen)

    def render(self, screen):
        super().render(screen)
        self.ref_point.render(screen)

