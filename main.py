import random
import logging
import pygame as pg
from pygame.locals import *
from sys import exit
from entity import Entity
from box import Box
from player import Player

WIDTH = 1200
HEIGHT = 650


def main():
    pg.init()
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    pg.display.set_caption("game made with pygame")
    clock = pg.time.Clock()

    # set background
    background = pg.image.load("design/background.png")
    background = pg.transform.scale(background, (WIDTH, HEIGHT))

    # create player
    player = Player()

    # create entity
    entity = Entity()

    # create box to hide the player
    box = Box()

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
            player.get_rect().move_ip(-1, 0)
            player.get_rect().clamp_ip(screen.get_rect())
        if pg.key.get_pressed()[K_RIGHT]:
            player.get_rect().move_ip(1, 0)
            player.get_rect().clamp_ip(screen.get_rect())

        # check if entity is going to wake up
        timestamp = pg.time.get_ticks() - entity.entity_previous_timestamp
        entity_timestamp = entity.get_entity_timestamp()
        if not entity.is_awake() and (
                timestamp == entity.get_entity_timestamp() or abs(timestamp - entity_timestamp) <= 15):
            print("waking up")
            entity.wake_up()

        if entity.is_awake() and abs(timestamp - entity_timestamp) >= 5000:
            print("coming back to sleep")
            entity.come_back_to_sleep()

        screen.blit(background, (0, 0))
        screen.blit(final_text, (1000, 40))  # the text-position is the position of the top-right corner
        entity.render(screen)  # experiment to draw the entity
        player.render(screen)
        box.render(screen)
        pg.display.update()


if __name__ == '__main__':
    main()
