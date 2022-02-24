from consts import Consts
from entity import Entity
import pygame as pg


class Observer:

    """
    A base class for the observer class
    """

    def on_notify(self, event):
        raise NotImplemented


class GameOverObserver(Observer):

    """
    A concrete observer class, used to handle the game over event

    Methods
    ----------

    on_notify(self, event)
        Checks the received event and handles it if it is the SET_GAME_OVER event
    """

    def on_notify(self, event):  # obj is, in this case, the bool that makes the game stop
        if event.name == Consts.SET_GAME_OVER:
            Consts.GAME_OVER = Consts.IS_GAME_OVER


class Subject:
    """
    A base class for the subject class

    Methods
    ----------
    add_observer(self, obs)
        Adds a new observer to the list of observers that the subject needs to notify

    remove_observer(self, obs)
        Removes the specified observer from the list

    notify(self, event)
        Sends the event to each subscribed observer
    """

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
    """
    Concrete subject class that checks the moment in which the event SET_GAME_OVER is created/fired
    It basically checks the collision between each laser and the obstacles

    Methods
    ----------
    update(self, hit_left, hit_right)
        Checks if it's time to fire the event SET_GAME_OVER by making the collisions between each laser and obstacles
    """
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
