# Imports from other modules
from physics.rigidbody import Rigidbody
from physics.collider2 import BoxCollider2
import settings as s
from physics.vector2 import Vector2
import physics.vector2 as vec



class Player(Rigidbody):
    '''
    This class handles the generic makeup of a character/player.
    This should be used as an abstract class and it should be extended.
    '''
    def __init__(self, x, y, key_bindings, **settings):
        '''
        Constructor.

        :param x: the starting x postion.
        :param y: the starting y position.
        :param key_bindings: the key bindings of the player.
        :param settings: a dictionary/**kwargs that stores mutable stats and abilities of different players.
        This should be tuned to balance the character stats.
        '''
        super().__init__(int(x), int(y), settings.get('mass', 10))
        self.key_bindings = key_bindings

        self.max_fallspeed = settings.get('max_fallspeed', 0.7)
        self.max_runspeed = settings.get('max_runspeed', 0.8)
        self.gravity_coef = settings.get('gravity_coef', 0.22)
        self.friction_coef = settings.get('friction_coef', 0.05)
        self.drag_coef = settings.get('drag_coef', 0.1)
        self.jump_force = settings.get('jump_force', Vector2(0, -10))
        self.run_force = settings.get('run_force', Vector2(0.3, 0))
        self.jumps = settings.get('jumps', 4)
        self.jumps_left = self.jumps

        # Basically acts as a stun duration
        self.frames_in_tumble = 0
        self.direction_facing = settings.get('direction_facing', 1)  # 1 for player facing right and -1 for player facing left
        self.grounded_on = None      # Holds obstacle if player is on a ground and None if in the air

        self.lives = 3
        self.damage_percentage = 0

        self.size = (settings.get('width',25), settings.get('height', 50))

        # The hitbox for the player.
        self.collider = BoxCollider2(self.position.x, self.position.y, self.position.x + self.size[0],
                                     self.position.y + self.size[1])

        # The hitbox for the attack if there is one.
        self.attack_collider = None

        # The previous hitbox for the player used for detecting collisions using interpolation.
        self.prev_collider = self.collider.clone()

    def draw(self, screen):
        print("You did not override this in the child class.")

    def update(self, time):
        super().update(time)

        # Update previous collider position for interpollation
        self.prev_collider.set_position(self.collider.p1.x, self.collider.p1.y)

        # Update collider position based on physics
        self.collider.set_position(int(self.position.x), int(self.position.y))

        # Update attack collider position and duration
        if self.attack_collider is not None:
            if self.attack_collider.total_lag <= 0:
                self.attack_collider = None
            else:
                self.attack_collider.set_position_from_player(self)
                self.attack_collider.total_lag -= vec.clamp(time * s.FPS / 1000, 0, 100000)

        # Update tumble/stun duration
        if self.frames_in_tumble > 0:
            self.frames_in_tumble -= time * s.FPS / 1000
            self.frames_in_tumble = vec.clamp(self.frames_in_tumble, 0, 100000)

        # Reset the player if out of bounds
        if self.position.y > 1400 or self.position.y < -300 or -300>self.position.x or self.position.x>2400:
            self.position.x = (1000)
            self.position.y = (400)
            self.lives += -1
            self.damage_percentage = 0
            self.frames_in_tumble = 0
