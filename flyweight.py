import random

import pygame as pg

from consts import Consts
from food import Food


class FoodSpawner:
    def __init__(self, minimal_bound, maximal_bound):
        self.foods = [Food(10, 10, Consts.FOOD_BREAD[0], Consts.FOOD_BREAD[1]),
                      Food(10, 10, Consts.FOOD_SOUP[0], Consts.FOOD_SOUP[1]),
                      Food(10, 10, Consts.FOOD_MEAT[0], Consts.FOOD_MEAT[1])]

        self.minimal_bound = minimal_bound
        self.maximal_bound = maximal_bound
        self.number_foods = 0
        self.food_list = pg.sprite.Group()
        self.counter = 0

    def select_new_food(self):
        random.shuffle(self.foods)
        random_food = random.choice(self.foods)
        new_food = random_food.clone()
        print(self.generate_random_position())
        new_food.set_pos(self.generate_random_position())
        return new_food

    def spawn_new_food(self):
        food = self.select_new_food()
        self.food_list.add(food)
        self.number_foods += 1

    def update(self, screen):
        self.food_list.draw(screen)

        if self.counter % 5 == 0:
            self.spawn_new_food()

        self.counter += 1

    def generate_random_position(self):
        return random.randrange(self.minimal_bound, self.maximal_bound), \
               random.randrange(self.minimal_bound, self.maximal_bound)

    def get_food_list(self):
        return self.food_list
