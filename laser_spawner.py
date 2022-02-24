from laser import Laser


class LaserSpawner:
    """
    A class to create a new laser, recurring to Prototype and Factory Method design patterns

    Methods
    ----------

    spawn_laser(self)
        Clones the laser given as parameter
    """

    def spawn_laser(self, prototype) -> Laser:
        """
       Parameters
       ----------

       prototype: Laser
            The laser that will be cloned

        Return
        ----------
        --> Laser
        """
        return prototype.clone()
