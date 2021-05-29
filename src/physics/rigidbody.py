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

    def add_gravity(self, gravity_coef):
        self.add_force(Vector2(0, gravity_coef))

    def add_friction(self, friction_coef):
        # Add friction from ground along x only
        friction = vec.multiply(vec.normalize(self.velocity), -friction_coef)
        friction.y = 0
        self.add_force(friction)

    def add_drag(self, drag_coef):
        if self.velocity.x != 0 or self.velocity.y != 0:
            speed = self.velocity.mag()
            drag = speed * speed * drag_coef
            direction = vec.multiply(self.velocity, -1)
            direction.normalize()
            self.add_force(vec.multiply(direction, drag))

    def reset_velocity(self):
        self.velocity.x = self.velocity.y = 0

    def update(self, time):
        self.velocity.add(self.acceleration)
        self.position.add(vec.multiply(self.velocity, time))
        self.acceleration.multiply(0)
