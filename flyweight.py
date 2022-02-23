import random

import pygame as pg

from box import Box
from consts import Consts
from food import Food


def check_collision_with_obstacles(new_food, obstacles_list):
    if pg.sprite.spritecollideany(new_food, obstacles_list):
        return True
    return False


class FoodSpawner:
    # each parameter is a tuple  with 2 values: minimal_bound and maximal_bound of each axis

    def __init__(self, bounds):
        self.foods = [Food(10, 10, Consts.AVAILABLE_FOODS.get(Consts.FOOD_BREAD)[0],
                           Consts.AVAILABLE_FOODS.get(Consts.FOOD_BREAD)[1]),
                      Food(10, 10, Consts.AVAILABLE_FOODS.get(Consts.FOOD_SOUP)[0],
                           Consts.AVAILABLE_FOODS.get(Consts.FOOD_SOUP)[1]),
                      Food(10, 10, Consts.AVAILABLE_FOODS.get(Consts.FOOD_MEAT)[0],
                           Consts.AVAILABLE_FOODS.get(Consts.FOOD_MEAT)[1])]

        self.bounds = bounds
        self.bounds_x = self.bounds[0]
        self.bounds_y = self.bounds[1]

        self.number_foods = 0
        self.food_list = pg.sprite.Group()
        self.counter = 0

    def select_new_food(self):
        random.shuffle(self.foods)
        random_food = random.choice(self.foods)
        new_food = random_food.clone()
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
        if self.counter % 100 == 0:
            if self.number_foods <= 10:
                self.spawn_new_food(obstacles_list)

        self.counter += 1

    def generate_random_position(self):
        return random.randrange(self.bounds_x[0], self.bounds_x[1]), \
               random.randrange(self.bounds_y[0], self.bounds_y[1])

    def get_food_list(self):
        return self.food_list


def check_collision_with_foods(new_box, food_list):
    if pg.sprite.spritecollideany(new_box, food_list):
        return True
    return False


class BoxSpawner:

    def __init__(self):
        self.boxes = [Box(10, 10, Consts.BOX_SIMPLE),
                      Box(10, 10, Consts.BOX_STATUE),
                      Box(10, 10, Consts.BOX_ANUBIS)]

        self.box_list = pg.sprite.Group()

    def select_new_box(self):
        random.shuffle(self.boxes)
        random_box = random.choice(self.boxes)
        new_box = random_box.clone()
        new_box.set_pos(self.generate_random_position())
        return new_box

    def spawn_new_box(self, obstacles_list):
        box = self.select_new_box()
        for x in range(5):
            if check_collision_with_foods(box) or check_collision_with_obstacles(box, obstacles_list):
                box = self.select_new_box()
            else:
                break
        self.box_list.add(box)

    def create_all_boxes(self, obstacles_list):
        for x in range(5):
            self.spawn_new_box(obstacles_list)

    def update(self, screen):
        self.box_list.draw(screen)

    def generate_random_position(self):
        return random.randrange(0, Consts.WIDTH - 50), random.randrange(0, Consts.HEIGHT - 50)
