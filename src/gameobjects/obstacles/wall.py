from src.gameobjects.obstacles.obstacles import Obstacle


class Wall(Obstacle):
    def __init__(self, x1, y1, x2, y2):
        super().__init__(x1, y1, x2, y2)