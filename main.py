import random

import pygame
from pygame.locals import *
from sys import exit

WIDTH = 1200
HEIGHT = 650


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("game made with pygame")
    clock = pygame.time.Clock()

    font = pygame.font.SysFont('arial', 30, True, False)
    score = 0

    while True:
        clock.tick(60)
        screen.fill("black")
        message = f'Score: {score}'
        final_text = font.render(message, False, 'white')

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

        screen.blit(final_text, (1000, 40))  # the text-position is the position of the top-right corner
        pygame.display.update()


if __name__ == '__main__':
    main()
