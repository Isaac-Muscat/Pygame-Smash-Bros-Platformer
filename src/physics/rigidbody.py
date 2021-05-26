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

    def reset_velocity(self):
        self.velocity.x = self.velocity.y = 0

    def update(self, clock):
        self.velocity.add(self.acceleration)
        self.position.add(vec.multiply(self.velocity, clock.get_time()))
        self.acceleration.multiply(0)
