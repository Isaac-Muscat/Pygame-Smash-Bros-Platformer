import physics.vector2 as vec
from physics.vector2 import Vector2


class Rigidbody(object):
    '''
    This class drives the physics engine. It should be used as an abstract class.
    Add forces and it attempts to modify the position, velocity, and acceleration
        of the object based on the time passed between frames
        according to Newton's Second and First Law of Motion
    '''
    def __init__(self, x, y, mass):
        self.mass = mass
        self.position = Vector2(x, y)
        self.velocity = Vector2(0, 0)
        self.acceleration = Vector2(0, 0)

    def add_force(self, force):
        '''
        Adds a force to the object.

        :param force: the vector to integrate into the acceleration
        :return: NA.
        '''
        self.acceleration.add(vec.divide(force, self.mass))

    def add_gravity(self, gravity_coef):
        # Adds gravitational force
        self.add_force(Vector2(0, gravity_coef))

    def add_friction(self, friction_coef):
        # Add friction from ground along x only
        vel_dir = vec.normalize(self.velocity).x
        if vel_dir > 0:
            friction = max(friction_coef * -vel_dir, -self.velocity.x)

        else:
            friction = min(friction_coef * -vel_dir, -self.velocity.x)

        self.add_force(Vector2(friction, 0))

    def add_drag(self, drag_coef):
        # Adds a drag force
        if self.velocity.x != 0 or self.velocity.y != 0:
            speed = self.velocity.mag()
            drag = speed * speed * drag_coef
            direction = vec.multiply(self.velocity, -1)
            direction.normalize()
            self.add_force(vec.multiply(direction, drag))

    def reset_velocity(self):
        # Resets the velocity of the object
        self.velocity.x = self.velocity.y = 0

    def update(self, time):
        '''
        This should only be called during update in scenes.py.
        Updates all aspects of an objects motion.

        :param time: the time in milliseconds since the last frame
        :return: NA.
        '''
        self.velocity.add(self.acceleration)
        self.position.add(vec.multiply(self.velocity, time))
        self.acceleration.multiply(0)
