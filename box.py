import pygame as pg


class Box(pg.sprite.Sprite):
    '''
    def __init__(self, screen, pos_x, pos_y):
        # call the parent class (Sprite) constructor
        super().__init__()

        self.screen = screen

        # store the desired position
        self.pos_x = pos_x
        self.pos_y = pos_y

        # create an image of the box
        self.image = pg.image.load("design/box.png")
        self.image.set_colorkey((0, 0, 0))

        # create a rect to track the position of the object
        self.rect = self.image.get_rect(topleft=(self.pos_x, self.pos_y))

        self.mask = pg.mask.from_surface(self.image)

    '''
    def __init__(self, screen):
        super().__init__()
        # self.image = pygame.Surface((50, 50))
        self.image = pg.image.load("design/box.png")
        self.image.set_colorkey((0, 0, 0))
        # pygame.draw.rect(self.image, (0, 0, 255), (0, 0, 50, 50))
        self.rect = self.image.get_rect(topleft=(1000, 526))
        # screen.blit(self.image, self.rect)

    def clone(self):
        # print("here")
        return Box(self.screen, self.pos_x, self.pos_y)

    def render(self, screen):
        screen.blit(self.image, self.rect)

    def set_x(self, new_x):
        self.pos_x = new_x
        self.set_rect(self.image.get_rect(topleft=(self.pos_x, self.pos_y)))

    def set_y(self, new_y):
        self.pos_y = new_y
        self.set_rect(self.image.get_rect(topleft=(self.pos_x, self.pos_y)))

    def set_pos(self, new_x, new_y):
        self.pos_x = new_x
        self.pos_y = new_y
        self.set_rect(self.image.get_rect(topleft=(self.pos_x, self.pos_y)))

    def set_rect(self, new_rect):
        self.rect = new_rect
