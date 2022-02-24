import pygame as pg


class Laser:
    """
    A class used to create lines that link each eye of the entity to the player
    Useful for collision purposes
    Recurring to Prototype and Update Method design patterns
    """

    def __init__(self, color, starting_point, ending_point, width=5):
        super().__init__()
        self.color = color
        self.starting_point = starting_point
        self.ending_point = ending_point
        self.width = width

    def check_collisions(self, box_list):
        # checks if there are points from the line given by the starting and ending points
        # inside the specified object aka box, the output gives the start and end points from the box that belong to the
        # line
        for box in box_list:
            if box.rect.clipline((self.starting_point, self.ending_point)) != ():
                return True
        return False

    def clone(self):
        return Laser(self.color, self.starting_point, self.ending_point, self.width)

    def update(self, screen, player):
        # update coordinates of laser
        self.set_ending_point(player.ref_point.get_pos())

    def set_ending_point(self, new_point):
        self.ending_point = new_point
