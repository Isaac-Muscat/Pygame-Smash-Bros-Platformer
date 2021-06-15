from gameobjects.obstacles.obstacles import Obstacle

# Potential for more functionality like ledge grabbing or passing through the ground.
# Not neccesary --> Obstacle would suffice.
class Platform(Obstacle):
    def __init__(self, x1, y1, x2, y2, color):
        super().__init__(int(x1), int(y1), int(x2), int(y2), color)