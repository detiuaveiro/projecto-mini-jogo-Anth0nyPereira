import pygame as pg


class Consts:
    """
    A class that stores some constants and pointers to some kind of information
    """

    WIDTH = 1200
    HEIGHT = 650

    # consts related to each type of food: image to sprite, number os points for score
    FOOD_BREAD = "FOOD_BREAD"
    FOOD_SOUP = "FOOD_SOUP"
    FOOD_MEAT = "FOOD_MEAT"

    AVAILABLE_FOODS = {FOOD_BREAD: [pg.image.load("design/bread.png"), 1], FOOD_SOUP: [pg.image.load("design/soup.png"), 5],
                       FOOD_MEAT: [pg.image.load("design/meat.png"), 20]}

    # consts related to food spawning
    FIRST_QUADRANT = (WIDTH // 2 + 1, WIDTH - 50), (80, HEIGHT // 2)
    SECOND_QUADRANT = (0, WIDTH // 2), (80, HEIGHT // 2)
    THIRD_QUADRANT = (0, WIDTH // 2), (HEIGHT // 2 + 1, HEIGHT - 50)
    FOURTH_QUADRANT = (WIDTH // 2 + 1, WIDTH - 50), (HEIGHT // 2 + 1, HEIGHT - 50)

    # consts related to each type of box
    BOX_SIMPLE = "BOX_SIMPLE"
    BOX_STATUE = "BOX_STATUE"
    BOX_ANUBIS = "BOX_ANUBIS"
    # there is the path to each sprite and its size (for resize purposes)
    AVAILABLE_BOXES = {BOX_SIMPLE: [pg.image.load("design/box.png"), (100, 40)],
                       BOX_STATUE: [pg.image.load("design/box2.png"), (60, 120)],
                       BOX_ANUBIS: [pg.image.load("design/box3.png"), (100, 100)]}

    # consts related to box spawning
    ALL_QUADRANT = (0, WIDTH - 150), (0, HEIGHT - 150)

    # const related to custom event type and handle events
    CUSTOM_GAME_EVENT = pg.event.custom_type()
    UPDATE_SCORE = 1
    SET_GAME_OVER = 2

    # const related to game over
    IS_NOT_GAME_OVER = False
    IS_GAME_OVER = True
    GAME_OVER = IS_NOT_GAME_OVER

    # consts related to path to load each remaining sprite
    SPRITE_PLAYER_WITHOUT_FOOD = pg.image.load("design/playerv1.png")
    SPRITE_PLAYER_WITH_FOOD = pg.image.load("design/playerwithfood.png")
    SPRITE_ENTITY_SLEEPING = pg.image.load("design/entity_sleepingv1.png")
    SPRITE_ENTITY_AWAKE = pg.image.load("design/entity_awakev1.png")
    SPRITE_SHELTER = pg.image.load("design/shelter.png")
    SPRITE_POINT = pg.image.load("design/point.png")
    SPRITE_BACKGROUND = pg.image.load("design/background.png")


