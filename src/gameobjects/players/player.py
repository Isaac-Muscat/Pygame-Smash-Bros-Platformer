from physics.rigidbody import Rigidbody
from physics.collider2 import BoxCollider2
import settings as s
import physics.vector2 as vec
from physics.vector2 import Vector2


class Player(Rigidbody):
    def __init__(self, x, y, width=25, height=50, mass=10, jumps=4,
                 drag_coef=0.3, friction_coef=0.05, gravity_coef=0.3, max_runspeed=0.5, max_fallspeed=0.7,
                 jump_force=Vector2(0, -10), run_force=Vector2(0.25, 0)):
        super().__init__(int(x), int(y), mass)

        self.max_fallspeed = max_fallspeed
        self.max_runspeed = max_runspeed
        self.gravity_coef = gravity_coef
        self.friction_coef = friction_coef
        self.drag_coef = drag_coef
        self.jump_force = jump_force
        self.run_force = run_force
        self.jumps = jumps
        self.jumps_left = jumps

        self.frames_in_tumble = 0
        self.direction_facing = 1  # 1 for player facing right and -1 for player facing left

        self.size = (width, height)
        self.collider = BoxCollider2(self.position.x, self.position.y, self.position.x + self.size[0],
                                     self.position.y + self.size[1])
        self.prev_collider = self.collider.clone()
        self.sprite = 'sprite path stuff'

    def draw(self):
        print("You did not override this in the child class.")

    def update(self, time):
        super().update(time)

        # Update prev collider position for interpollation
        self.prev_collider.set_position(self.collider.p1.x, self.collider.p1.y)

        # Update collider position based on physics
        self.collider.set_position(int(self.position.x), int(self.position.y))

        # Update tumble/stun duration
        if self.frames_in_tumble > 0:
            self.frames_in_tumble -= time * s.FPS / 1000

    def normal_attack(self):
        pass

    def special_attack(self):
        pass
