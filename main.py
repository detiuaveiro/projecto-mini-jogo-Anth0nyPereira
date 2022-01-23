import random
import logging
import pygame as pg
from pygame.locals import *
from sys import exit

from command import InputHandler
from entity import Entity
from box import Box
from food import Food
from laser import Laser
from player import Player
from point import Point
from prototype import BoxSpawner, LaserSpawner

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
    player = Player(1100, 550)

    # create entity
    entity = Entity()

    # create box to hide the player
    box_list = pg.sprite.Group()
    box = Box(screen)
    # box = Box(screen, 1000, 526)
    box_list.add(box)

    # create food
    food = Food(screen)
    food_lst = pg.sprite.Group()
    food_lst.add(food)

    # experiment to create a box spawner
    # box_spawner = BoxSpawner()
    # box2 = box_spawner.spawn_box(box)
    # print(f'{box2.pos_x} - {box2.pos_y}')
    # box2.set_pos(400, 526)

    # experiment to create a laser spawner
    laser_left = Laser("red", entity.get_left_point_coords(), player.ref_point.get_pos())
    laser_right = Laser("red", entity.get_right_point_coords(), player.ref_point.get_pos())
    laser_spawner = LaserSpawner()

    font = pg.font.SysFont('arial', 30, True, False)
    score = 0

    running = True
    game_over = False

    while running:
        clock.tick(60)
        screen.fill("black")
        if game_over:
            # print(pg.font.get_fonts())
            font = pg.font.SysFont('michroma', 80, True, False)
            game_over_msg = "Game Over"
            game_over_txt = font.render(game_over_msg, False, 'red')
            screen.blit(game_over_txt, (game_over_txt.get_rect(center=(WIDTH // 2, 100))))
            for event in pg.event.get():
                if event.type == QUIT:
                    pg.quit()
                    exit()
            pg.display.update()
        else:
            message = f'Score: {score}'
            final_text = font.render(message, False, 'white')

            for event in pg.event.get():
                if event.type == QUIT:
                    pg.quit()
                    exit()

            '''
            if pg.key.get_pressed()[K_LEFT]:
                player.get_rect().move_ip(-1, 0)
                player.get_rect().clamp_ip(screen.get_rect())
            if pg.key.get_pressed()[K_RIGHT]:
                player.get_rect().move_ip(1, 0)
                player.get_rect().clamp_ip(screen.get_rect())
                
            '''

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
            '''
            # check if player collides with box
            box_hit_lst = pg.sprite.spritecollide(player, box_list, False)
            if entity.is_awake() and not box_hit_lst:  # if list is empty, no collision, so game over
                print("Game Over")
                game_over = True
            '''

            screen.blit(background, (0, 0))
            screen.blit(final_text, (1000, 40))  # the text-position is the position of the top-right corner
            entity.render(screen)  # experiment to draw the entity
            player.render(screen)

            for fd in food_lst:
                fd.render(screen)
            # box.render(screen)
            # box2.render(screen)

            # create laser experiment
            # laser_left = Laser()
            # laser_left = Laser("red", entity.get_left_point_coords(), player.ref_point.get_pos())
            # laser_left.render(screen)

            # laser_right = Laser()
            # laser_right = Laser("red", entity.get_right_point_coords(), player.ref_point.get_pos())
            # laser_right.render(screen)

            laser_left.set_ending_point(player.ref_point.get_pos())
            laser_right.set_ending_point(player.ref_point.get_pos())
            laser_left = laser_spawner.spawn_laser(laser_left)
            laser_right = laser_spawner.spawn_laser(laser_right)
            '''
            group = pg.sprite.Group([box, laser_left, laser_right])
            group.draw(screen)
            '''
            laser_left.render(screen)
            laser_right.render(screen)
            box.render(screen)
            hit_left = pg.sprite.collide_mask(laser_left, box)
            hit_right = pg.sprite.collide_mask(laser_right, box)


            # collision with food test
            player.update(food_lst)
            print(food_lst)

            # collisions algorithm

            for box in box_list:
                if entity.is_awake() and not hit_left and not hit_right:
                    print("Game Over")
                    game_over = True

            pg.display.flip()
            pg.display.update()

            # call inputHandler
            InputHandler(screen).handle_input(player)
            InputHandler(screen).handle_input(player.ref_point)


if __name__ == '__main__':
    main()
