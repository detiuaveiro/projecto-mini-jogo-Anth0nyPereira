from box import Box
from laser import Laser


class BoxSpawner:

    def spawn_box(self, prototype) -> Box:
        return prototype.clone()


class LaserSpawner:

    def spawn_laser(self, prototype) -> Laser:
        return prototype.clone()
