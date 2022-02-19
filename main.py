import random
import logging
import pygame as pg
from pygame.locals import *
from sys import exit

from command import InputHandler
from entity import Entity
from box import Box
from food import Food
from game_manager import GameManager
from laser import Laser
from player import Player
from point import Point
from prototype import BoxSpawner, LaserSpawner



def main():
    pg.init()

    gm = GameManager()
    gm.run()


if __name__ == '__main__':
    main()
