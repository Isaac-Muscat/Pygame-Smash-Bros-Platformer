from physics.rigidbody import Rigidbody
from physics.collider2 import SpriteCollider2, BoxCollider2
import settings as s
import physics.vector2 as vec
from physics.vector2 import Vector2
import pygame
from Sprites import jonahSprites

class Player(Rigidbody):
    def __init__(self, x=s.s_s[0] / 2, y=100, width=25, height=50, mass=10, jumps=4,
                 drag_coef=0.3, friction_coef=0.05,gravity_coef=0.3, max_runspeed=0.5,
                 jump_force=Vector2(0, -12), run_force=Vector2(0.25, 0)):
        super().__init__(x, y, mass)

        self.max_runspeed = max_runspeed
        self.gravity_coef = gravity_coef
        self.friction_coef = friction_coef
        self.drag_coef = drag_coef
        self.jump_force = jump_force
        self.run_force = run_force
        self.jumps = jumps
        self.jumps_left = jumps

        self.frames_in_tumble = 0
        self.direction_facing = 1 #1 for player facing right and -1 for player facing left

        self.size = (width, height)
        self.collider = SpriteCollider2(self.position.x, self.position.y, self.position.x + self.size[0], self.position.y + self.size[1])
        self.prev_collider = self.collider.clone()



    def draw(self, screen):
        #TODO sprite stuff here
        self.all_sprites_list = pygame.sprite.Group()
        self.stand = jonahSprites.Jonah(150, 150, self.position.x - 75, self.position.y - 75)

        self.all_sprites_list.add(self.stand)

        self.collider.draw_collider(screen, self.all_sprites_list)



    def update(self, time):
        super().update(time)

        #Update prev collider position for interpollation
        self.prev_collider.set_position(self.collider.p1.x, self.collider.p1.y)

        #Update collider position based on physics
        self.collider.set_position(self.position.x, self.position.y)

        #Update tumble/stun duration
        if self.frames_in_tumble > 0:
            self.frames_in_tumble -= time*s.FPS/1000

    def normal_attack(self):
        pass

    def special_attack(self):
        pass