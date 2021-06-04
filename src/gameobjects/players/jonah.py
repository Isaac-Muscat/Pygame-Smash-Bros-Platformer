from player import Player
import physics.vector2 as vec
import pygame


class Jonah(Player):
    def __init__(self, x, y, key_bindings):
        super().__init__(x, y, key_bindings)
        self.sprites = {'jump':pygame.image.load("sprites/Jonah/jump1.png"),
                        'walk':[pygame.image.load("sprites/Jonah/walk2.png"), pygame.image.load("sprites/Jonah/stand1.png")],
                        'stand':pygame.image.load("sprites/Jonah/stand1.png"),
                        'attack':pygame.image.load("sprites/Jonah/latk.png")}

        self.frame_count = 0
        self.time_between_frames = 10

    def process_inputs(self, event_keys, keys):
        for key in event_keys:
            if key == self.key_bindings['up'] and self.jumps_left > 1 and self.frames_in_tumble == 0:
                self.jumps_left -= 1
                self.velocity.y = 0
                self.add_force(self.jump_force)
                self.grounded = False
            if key == self.key_bindings['down'] and self.frames_in_tumble == 0:
                self.velocity.y = 0
                self.add_force(vec.multiply(self.jump_force, -0.5))
            if key == self.key_bindings['attack'] and self.frames_in_tumble == 0 and self.attack_frames == 0:
                self.attack_frames = 15

        if keys[self.key_bindings['left']] and self.velocity.x > -self.max_runspeed and self.frames_in_tumble == 0:
            if self.velocity.x>0 and self.grounded:
                run_force = vec.multiply(self.run_force, -5)
            else:
                run_force = vec.multiply(self.run_force, -1)
            self.add_force(run_force)
            self.direction_facing = -1

        if keys[self.key_bindings['right']] and self.velocity.x < self.max_runspeed and self.frames_in_tumble == 0:
            if self.velocity.x < 0 and self.grounded:
                run_force = vec.multiply(self.run_force, 5)
            else:
                run_force = self.run_force
            self.add_force(run_force)
            self.direction_facing = 1

    def draw(self, screen):

        if self.attack_frames > 0:
            self.image = self.sprites['attack']
        # In the air
        elif not self.grounded:
            self.image = self.sprites['jump']
        # Walking
        elif round(self.velocity.x, 1) != 0:
            self.image = self.sprites['walk'][self.frame_count//self.time_between_frames]
            self.frame_count += 1
            if self.frame_count >= self.time_between_frames*len(self.sprites['walk']):
                self.frame_count = 0
        # Stationary
        else:
            self.image = self.sprites['stand']

        self.image = pygame.transform.scale(self.image, (150, 150))
        # Change direction of sprites
        if self.direction_facing == -1:
            self.image = pygame.transform.flip(self.image, True, False)
        screen.blit(self.image, [self.position.x - 75, self.position.y - 75])


