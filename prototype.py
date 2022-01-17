from box import Box


class BoxSpawner:

    def spawn_box(self, prototype) -> Box:
        return prototype.clone()


