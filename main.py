import random

import pygame as pg
from pygame.locals import *
from sys import exit

WIDTH = 1200
HEIGHT = 650


def main():
    pg.init()
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    pg.display.set_caption("game made with pygame")
    clock = pg.time.Clock()

    # load entity images
    entity_awake = pg.image.load("design/entity_awakev1.png")

    font = pg.font.SysFont('arial', 30, True, False)
    score = 0

    while True:
        clock.tick(60)
        screen.fill("black")
        message = f'Score: {score}'
        final_text = font.render(message, False, 'white')

        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                exit()

        screen.blit(final_text, (1000, 40))  # the text-position is the position of the top-right corner
        screen.blit(entity_awake, (500, 40)) # experiment to draw the entity
        pg.display.update()


if __name__ == '__main__':
    main()
