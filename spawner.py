import random
import pygame as pg
from abc import ABC, abstractmethod


class Spawner(ABC):
    """
    An abstract class used to represent a spawner of specific objects, such as food.

    Attributes
    ----------

    all_objs_from_sprites: Group()
            a list containing all sprites from the game (except the player), so that the spawning of new
            objects doesn't overlap another sprite that exists already on that place


    Methods
    ----------


    """

    all_objs_from_sprites = pg.sprite.Group() # make this list static

    @abstractmethod
    def __init__(self, objects, bounds, entity_shelter_list):
        """
        Parameters
        ----------

        objects: list
                all available objects from what we can spawn a new object. where it is implemented the flyweight design pattern

        bounds: tuple
                a tuple consisting of 2 tuples. the first is the min_boundary and max_boundary for the X-AXIS. the other one is related to the Y_AXIS

        entity_shelter_list: Group()
                a list with the entity and shelter sprites

        """
        self.objects = objects # available different objects, for instance, 3 food, 3 boxes
        self.bounds = bounds

        self.bounds_x = self.bounds[0]
        self.bounds_y = self.bounds[1]

        self.entity_shelter_lst = entity_shelter_list

        for element in self.entity_shelter_lst:
            Spawner.all_objs_from_sprites.add(element)

        self.counter = 0

    def select_new_object(self):
        random.shuffle(self.objects)
        random_object = random.choice(self.objects)
        new_object = random_object.clone()
        new_object.set_pos(self.generate_random_position())
        return new_object

    def spawn_new_object(self): # obstacles_list is sum of all boxes, food, entity and shelter together
        obj = self.select_new_object()
        for x in range(5):
            if self.check_collision_with_others(obj):
                obj = self.select_new_object()
            else:
                break
        Spawner.all_objs_from_sprites.add(obj)
        return obj

    def check_collision_with_others(self, new_obj):
        """
        Parameters
        ----------

        objects: list
        """
        if pg.sprite.spritecollideany(new_obj, Spawner.all_objs_from_sprites):
            return True
        return False

    @abstractmethod
    def update(self, screen):
        # Spawner.all_objs_from_sprites.draw(screen)
        # print("spawner update method called")
        raise NotImplemented

    def generate_random_position(self):
        return random.randrange(self.bounds_x[0], self.bounds_x[1]), \
               random.randrange(self.bounds_y[0], self.bounds_y[1])
