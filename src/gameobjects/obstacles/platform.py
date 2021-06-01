from gameobjects.obstacles.obstacles import Obstacle


class Platform(Obstacle):
    def __init__(self, x1, y1, x2, y2):
        super().__init__(int(x1), int(y1), int(x2), int(y2))
