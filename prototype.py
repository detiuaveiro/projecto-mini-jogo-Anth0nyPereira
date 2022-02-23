from laser import Laser


class LaserSpawner:

    def spawn_laser(self, prototype) -> Laser:
        return prototype.clone()
