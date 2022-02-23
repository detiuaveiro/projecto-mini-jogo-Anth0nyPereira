from consts import Consts
from food import Food
from spawner import Spawner
import pygame as pg


def get_food_list():
    return FoodSpawner.all_foods


class FoodSpawner(Spawner):
    # each parameter is a tuple  with 2 values: minimal_bound and maximal_bound of each axis

    all_foods = pg.sprite.Group()

    def __init__(self, bounds, entity_shelter_list):

        super().__init__([Food(10, 10, Consts.AVAILABLE_FOODS.get(Consts.FOOD_BREAD)[0],
                               Consts.AVAILABLE_FOODS.get(Consts.FOOD_BREAD)[1]),
                          Food(10, 10, Consts.AVAILABLE_FOODS.get(Consts.FOOD_SOUP)[0],
                               Consts.AVAILABLE_FOODS.get(Consts.FOOD_SOUP)[1]),
                          Food(10, 10, Consts.AVAILABLE_FOODS.get(Consts.FOOD_MEAT)[0],
                               Consts.AVAILABLE_FOODS.get(Consts.FOOD_MEAT)[1])],
                         bounds,
                         entity_shelter_list)

        self.bounds = bounds
        self.bounds_x = self.bounds[0]
        self.bounds_y = self.bounds[1]

        self.number_foods = 0
        self.food_list = pg.sprite.Group()
        self.counter = 0

    def spawn_new_object(self):
        food = super().spawn_new_object()
        FoodSpawner.all_foods.add(food)
        self.number_foods += 1
        # print(Spawner.all_objs_from_sprites)

    def update(self, screen):
        super().update(screen)
        if self.counter % 100 == 0:
            if self.number_foods <= 10:
                self.spawn_new_object()

        self.counter += 1