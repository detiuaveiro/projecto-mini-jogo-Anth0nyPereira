import random

import pygame as pg

from consts import Consts
from food import Food


def check_collision_with_obstacles(new_food, obstacles_list):
    if pg.sprite.spritecollideany(new_food, obstacles_list):
        return True
    return False


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

    def spawn_new_food(self, obstacles_list):
        food = self.select_new_food()
        for x in range(5):
            if self.check_collision_with_foods(food) or check_collision_with_obstacles(food, obstacles_list):
                food = self.select_new_food()
            else:
                break
        self.food_list.add(food)
        self.number_foods += 1

    def check_collision_with_foods(self, new_food):
        if pg.sprite.spritecollideany(new_food, self.food_list):
            return True
        return False

    def update(self, screen, obstacles_list):
        self.food_list.draw(screen)
        if self.counter % 50 == 0:
            if self.number_foods <= 20:
                self.spawn_new_food(obstacles_list)

        self.counter += 1

    def generate_random_position(self):
        return random.randrange(self.minimal_bound, self.maximal_bound), \
               random.randrange(self.minimal_bound, self.maximal_bound)

    def get_food_list(self):
        return self.food_list
