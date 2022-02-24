
import pygame as pg
from game_manager import GameManager


def main():
    pg.init()

    gm = GameManager.get_instance()
    gm.run()


if __name__ == '__main__':
    main()
