from consts import Consts
from food import Food
from spawner import Spawner
import pygame as pg


def get_food_list():
    """
    Return
    ----------
        --> pygame.Group
    """
    return FoodSpawner.all_foods


class FoodSpawner(Spawner):
    # each parameter is a tuple  with 2 values: minimal_bound and maximal_bound of each axis

    """
    A concrete spawner class used to spawn food in a specific boundary/quadrant/area of the window
    Recurring to Flyweight, Prototype and Update Method design patterns

    Attributes
    ----------

    all_foods: pygame.Group
            a list containing all sprite food from the game

    Methods
    ----------

    spawn_new_object(self)
        Selects a food and adds it to the list

    render(self, screen)
        Draws all food sprites on screen

    update(self, screen)
        Where the spawning of food take place

    Functions
    ----------

    get_food_list()
        Returns the list containing all food
    """

    all_foods = pg.sprite.Group()

    def __init__(self, bounds, entity_shelter_list):
        """
               Parameters
               ----------

               bounds: tuple
                       a tuple consisting of 2 tuples. the first is the min_boundary and max_boundary for the X-AXIS.
                       the other one is related to the Y_AXIS

               entity_shelter_list: pygame.Group
                       a list with the entity and shelter sprites

        """

        super().__init__([Food(10, 10, Consts.AVAILABLE_FOODS.get(Consts.FOOD_BREAD)[0],
                               Consts.AVAILABLE_FOODS.get(Consts.FOOD_BREAD)[1]),
                          Food(10, 10, Consts.AVAILABLE_FOODS.get(Consts.FOOD_SOUP)[0],
                               Consts.AVAILABLE_FOODS.get(Consts.FOOD_SOUP)[1]),
                          Food(10, 10, Consts.AVAILABLE_FOODS.get(Consts.FOOD_MEAT)[0],
                               Consts.AVAILABLE_FOODS.get(Consts.FOOD_MEAT)[1])],
                         bounds,
                         entity_shelter_list)

        self.number_foods = 0
        self.counter = 0

    def spawn_new_object(self):
        food = super().spawn_new_object()
        FoodSpawner.all_foods.add(food)
        self.number_foods += 1

    def render(self, screen):
        FoodSpawner.all_foods.draw(screen)

    def update(self, screen):
        if self.counter % 100 == 0:
            if self.number_foods <= 4:
                self.spawn_new_object()

        self.counter += 1
        self.render(screen)
