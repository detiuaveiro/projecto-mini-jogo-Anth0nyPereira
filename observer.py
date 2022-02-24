from consts import Consts
from entity import Entity
import pygame as pg


class Observer:

    def on_notify(self, event):
        raise NotImplemented


class GameOverObserver(Observer):

    def on_notify(self, event):  # obj is, in this case, the bool that makes the game stop
        if event.name == Consts.SET_GAME_OVER:
            Consts.GAME_OVER = Consts.IS_GAME_OVER


class Subject:

    def __init__(self):
        self.observers = []

    def add_observer(self, obs: Observer):
        self.observers.append(obs)

    def remove_observer(self, obs: Observer):
        self.observers.remove(obs)

    def notify(self, event):
        for obs in self.observers:
            obs.on_notify(event)


class GameOverSubject(Subject):
    def __init__(self):
        super().__init__()

        self.entity = Entity.get_instance()

    def update(self, hit_left, hit_right):
        # collisions algorithm
        if self.entity.is_awake() and not hit_left and not hit_right:

            # call set_game_over event
            ev = pg.event.Event(Consts.CUSTOM_GAME_EVENT,
                                {"name": Consts.SET_GAME_OVER})
            # pg.event.post(ev)
            self.notify(ev)
