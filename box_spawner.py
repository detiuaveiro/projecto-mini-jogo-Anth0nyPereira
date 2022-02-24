from box import Box
from consts import Consts
from spawner import Spawner
import pygame as pg


def get_box_list():
    """
    Return
    ----------
        --> Group()
    """
    return BoxSpawner.all_boxes


class BoxSpawner(Spawner):
    """
    A concrete spawner class used to spawn boxes on all screen

    Attributes
    ----------

    all_boxes: Group()
            a list containing all sprite boxes from the game

    Methods
    ----------

    spawn_new_object(self)
        Selects a box and adds it to the list

    create_all_boxes(self)
        Creates all boxes at the beginning

    render(self, screen)
        Draws all box sprites on screen

    update(self, screen)
        Just calls render method


    Functions
    ----------

    get_box_list()
        Returns the list containing all boxes
    """
    all_boxes = pg.sprite.Group()

    def __init__(self, bounds, entity_shelter_list):
        """
       Parameters
       ----------

       bounds: tuple
               a tuple consisting of 2 tuples. the first is the min_boundary and max_boundary for the X-AXIS.
               the other one is related to the Y_AXIS

       entity_shelter_list: Group()
               a list with the entity and shelter sprites

       """
        super().__init__([Box(10, 10, Consts.AVAILABLE_BOXES.get(Consts.BOX_SIMPLE)[0], Consts.AVAILABLE_BOXES.get(Consts.BOX_SIMPLE)[1]),
                          Box(10, 10, Consts.AVAILABLE_BOXES.get(Consts.BOX_STATUE)[0], Consts.AVAILABLE_BOXES.get(Consts.BOX_STATUE)[1]),
                          Box(10, 10, Consts.AVAILABLE_BOXES.get(Consts.BOX_ANUBIS)[0], Consts.AVAILABLE_BOXES.get(Consts.BOX_ANUBIS)[1])],
                         bounds,
                         entity_shelter_list)

    def spawn_new_object(self):
        box = super().spawn_new_object()
        BoxSpawner.all_boxes.add(box)

    def create_all_boxes(self):
        for x in range(5):
            self.spawn_new_object()

    def render(self, screen):
        BoxSpawner.all_boxes.draw(screen)

    def update(self, screen):
        self.render(screen)
