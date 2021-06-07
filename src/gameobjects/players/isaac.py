from player import Player
import physics.vector2 as vec
import settings as s
import pygame


class Isaac(Player):
    def __init__(self, x, y, key_bindings, **settings):
        super().__init__(x, y, key_bindings, **settings)

    def process_inputs(self, event_keys, keys):
        for key in event_keys:
            if key == self.key_bindings['up'] and self.jumps_left > 1 and self.frames_in_tumble == 0:
                self.jumps_left -= 1
                self.velocity.y = 0
                self.add_force(self.jump_force)

            if key == self.key_bindings['down'] and self.frames_in_tumble == 0:
                self.velocity.y = 0
                self.add_force(vec.multiply(self.jump_force, -0.5))

        if keys[self.key_bindings['left']] and self.velocity.x > -self.max_runspeed and self.frames_in_tumble == 0:
            run_force = vec.multiply(self.run_force, -1)
            self.add_force(run_force)
            self.direction_facing = -1

        if keys[self.key_bindings['right']] and self.velocity.x < self.max_runspeed and self.frames_in_tumble == 0:
            run_force = self.run_force
            self.add_force(run_force)
            self.direction_facing = 1

    def draw(self, screen):
        # TODO sprite stuff here
        self.collider.draw_collider(screen, s.BLUE)