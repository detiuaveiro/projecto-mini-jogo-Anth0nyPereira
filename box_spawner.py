from box import Box
from consts import Consts
from spawner import Spawner
import pygame as pg


def get_box_list():
    return BoxSpawner.all_boxes


class BoxSpawner(Spawner):
    all_boxes = pg.sprite.Group()

    def __init__(self, bounds, entity_shelter_list):
        super().__init__([Box(10, 10, Consts.BOX_SIMPLE),
                          Box(10, 10, Consts.BOX_STATUE),
                          Box(10, 10, Consts.BOX_ANUBIS)],
                         bounds,
                         entity_shelter_list)

    def spawn_new_object(self):
        box = super().spawn_new_object()
        BoxSpawner.all_boxes.add(box)

    def create_all_boxes(self):
        for x in range(5):
            self.spawn_new_object()

    def update(self, screen):
        super().update(screen)
