from physics.rigidbody import Rigidbody
from physics.collider2 import BoxCollider2
import settings as s
import physics.vector2 as vec
from physics.vector2 import Vector2

class Player(Rigidbody):
    def __init__(self, x=s.s_s[0] / 2, y=100, width=25, height=50, mass=10,
                 jumps=4, max_fall_vel=20, max_run_vel=7,
                 gravity=Vector2(0, 0.4), jump_force=Vector2(0, -12), run_force=Vector2(0.25, 0)):
        super().__init__(x, y, mass)

        self.jumps = jumps
        self.max_fall_vel = max_fall_vel
        self.max_run_vel = max_run_vel
        self.gravity = gravity
        self.jump_force = jump_force
        self.run_force = run_force

        self.frames_in_tumble = 0
        self.jumps_left = jumps

        self.size = (width, height)
        self.collider = BoxCollider2(self.position.x, self.position.y, self.position.x + self.size[0], self.position.y + self.size[1])
        self.sprite = 'sprite path stuff'

    def draw(self, screen):
        self.collider.draw_collider(screen, s.RED)

    def update(self, clock):
        # Apply drag force
        if self.velocity.x !=0 or self.velocity.y != 0:
            speed = self.velocity.mag()
            drag = speed * speed * 0.03 * clock.get_time()
            direction = vec.multiply(self.velocity, -1)
            direction.normalize()
            self.add_force(vec.multiply(direction, drag))
        super().update(clock)


        #Update collider position
        self.collider.set_position(self.position.x, self.position.y)

        #Update tumble/stun duration
        if self.frames_in_tumble > 0:
            self.frames_in_tumble-=1


class Ground(BoxCollider2):
    def __init__(self, x1, y1, x2, y2):
        super().__init__(x1, y1, x2, y2)

    def player_collided_from_top(self, player):
        '''
        Used to detect wheather a player has landed on top the platform or is touching it will falling off a cliff

        :param player: the player rigidbody being tested
        :return: True if player landed ontop and False if player collided with ground from the side
        '''
        if not player.collider.p2.x < self.p1.x and not player.collider.p1.x > self.p2.x and player.collider.p1.y<self.p1.y:
            if self.collider_has_collided(player.collider):
                return True
        return False
