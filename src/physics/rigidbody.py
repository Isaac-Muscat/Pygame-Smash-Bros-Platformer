import src.physics.vector2 as vec
from src.physics.vector2 import Vector2

class Rigidbody(object):
    def __init__(self, x, y, mass):
        self.mass = mass
        self.position = Vector2(x, y)
        self.velocity = Vector2(0, 0)
        self.acceleration = Vector2(0, 0)

    def add_force(self, force):
        self.acceleration.add(vec.divide(force, self.mass))

    def update(self):
        self.velocity.add(self.acceleration)
        self.position.add(self.velocity)
        self.acceleration.multiply(0)