import pygame as pg


class Point(pg.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.pos_x = pos[0]
        self.pos_y = pos[1]

        self.image = pg.image.load("design/point.png")

        # create a rect to track the position of the object
        self.rect = self.image.get_rect(topleft=(self.pos_x, self.pos_y))

    def scale(self, new_width, new_height):
        pg.transform.scale(self.image, (new_width, new_height))

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

    def get_rect(self):
        return self.rect

    def get_pos(self):
        return self.pos_x, self.pos_y

    def set_pos(self, new_pos):
        self.pos_x = new_pos[0]
        self.pos_y = new_pos[1]

    def set_rect(self, new_rect):
        self.rect = new_rect