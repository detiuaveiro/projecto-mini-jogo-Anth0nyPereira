from consts import Consts
from sprite import MoveableSprite


class Point(MoveableSprite):
    """
    A concrete moveable sprite class that represents a reference point used as a pivot to calculate the starting positions and
        ending positions of each Laser (they are helpful to make the collision and the "Player hides behind a box" mechanic
    Recurring to Subclass Sandbox pattern
    """

    def __init__(self, pos_x, pos_y):
        """
        Parameters
        ----------

        pos_x: int
               the first coordinate of the position of the pivot

        pos_y: int
                the second coordinate of the position of the pivot

        """
        super().__init__(pos_x, pos_y, Consts.SPRITE_POINT, Consts.SPRITE_POINT
                         .get_rect(topleft=(pos_x, pos_y)))

    def get_rect(self):
        return self.rect

    def get_pos(self):
        return self.pos_x, self.pos_y

    def set_pos(self, new_pos):
        self.pos_x = new_pos[0]
        self.pos_y = new_pos[1]

    def set_rect(self, new_rect):
        self.rect = new_rect
