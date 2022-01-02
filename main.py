import random

import pygame as pg
from pygame.locals import *
from sys import exit
from entity import Entity

WIDTH = 1200
HEIGHT = 650


def main():
    pg.init()
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    pg.display.set_caption("game made with pygame")
    clock = pg.time.Clock()

    # create player
    player = pg.image.load(("design/playerv1.png"))
    player_rect = player.get_rect(topleft=(1100, 550)) # it's actually left and then top

    # create entity
    entity = Entity()

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

        if pg.key.get_pressed()[K_LEFT]:
            player_rect.move_ip(-1, 0)
            player_rect.clamp_ip(screen.get_rect())
        if pg.key.get_pressed()[K_RIGHT]:
            player_rect.move_ip(1, 0)
            player_rect.clamp_ip(screen.get_rect())

        screen.blit(final_text, (1000, 40))  # the text-position is the position of the top-right corner
        entity.render(screen) # experiment to draw the entity
        screen.blit(player, player_rect)
        pg.display.update()


if __name__ == '__main__':
    main()
