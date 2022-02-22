import pygame as pg


class Consts:
    WIDTH = 1200
    HEIGHT = 650

    # conts related to each type of food: image to sprite, number os points for score
    FOOD_BREAD = pg.image.load("design/bread.png"), 1
    FOOD_SOUP = pg.image.load("design/soup.png"), 5
    FOOD_MEAT = pg.image.load("design/meat.png"), 20
