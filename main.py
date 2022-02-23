
import pygame as pg
from game_manager import GameManager


def main():
    pg.init()

    gm = GameManager()
    gm.run()


if __name__ == '__main__':
    main()
