from box import Box
from consts import Consts
from spawner import Spawner
import pygame as pg


def get_box_list():
    return BoxSpawner.all_boxes


class BoxSpawner(Spawner):
    all_boxes = pg.sprite.Group()

    def __init__(self, bounds, entity_shelter_list):
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
