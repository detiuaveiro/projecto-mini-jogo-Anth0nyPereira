import pygame as pg

from point import Point


class Player(pg.sprite.Sprite):

    def __init__(self, pos_x, pos_y):
        # call the parent class (Sprite) constructor
        super().__init__()

        # initialize parameters
        self.pos_x = pos_x
        self.pos_y = pos_y

        # create an image of the box
        self.image = pg.image.load("design/playerv1.png")

        # create a rect to track the position of the object
        self.rect = self.image.get_rect(topleft=(self.pos_x, self.pos_y))  # it's actually left and then top

        # create a point to use it for the collision algorithm
        self.ref_point = Point((self.pos_x + 15, self.pos_y + 15))

        # initialize pointer to picked food
        self.food = None

    def move_left(self, screen):
        # print("move left")
        vector = (-5, 0)
        self.get_rect().move_ip(-5, 0)
        # print(self.object.get_pos())
        self.set_pos((self.get_pos()[0] + vector[0], self.get_pos()[1] + vector[1]))
        self.get_rect().clamp_ip(screen.get_rect())

    def move_right(self, screen):
        # print("move right")
        vector = (5, 0)
        self.get_rect().move_ip(5, 0)
        self.set_pos((self.get_pos()[0] + vector[0], self.get_pos()[1] + vector[1]))
        self.get_rect().clamp_ip(screen.get_rect())

    def move_up(self, screen):
        vector = (0, -5)
        self.get_rect().move_ip(0, -5)
        self.set_pos((self.get_pos()[0] + vector[0], self.get_pos()[1] + vector[1]))
        self.get_rect().clamp_ip(screen.get_rect())

    def move_down(self, screen):
        vector = (0, 5)
        self.get_rect().move_ip(0, 5)
        self.set_pos((self.get_pos()[0] + vector[0], self.get_pos()[1] + vector[1]))
        self.get_rect().clamp_ip(screen.get_rect())

    def render(self, screen):
        screen.blit(self.image, self.rect)
        self.ref_point.render(screen)

    def update(self, food_list, shelter):
        food_hit = pg.sprite.spritecollideany(self, food_list)
        shelter_hit = self.get_rect().colliderect(shelter.reference_rect)
        if self.food is None and food_hit:
            self.food = food_hit
            self.image = pg.image.load("design/playerwithfood.png")
            food_hit.kill()
            pg.display.update()

        if self.food is not None and shelter_hit:
            self.food = None
            self.image = pg.image.load("design/playerv1.png")
            pg.display.update()

    def get_rect(self):
        return self.rect

    def get_pos(self):
        return self.pos_x, self.pos_y

    def set_pos(self, new_pos):
        self.pos_x = new_pos[0]
        self.pos_y = new_pos[1]
        # self.set_rect(self.image.get_rect(topleft=(self.pos_x, self.pos_y)))
        # self.ref_point.set_rect(self.image.get_rect(topleft=(self.pos_x, self.pos_y)))

    def set_rect(self, new_rect):
        self.rect = new_rect
