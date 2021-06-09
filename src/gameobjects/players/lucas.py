from gameobjects.players.player import Player
import physics.vector2 as vec
import gameobjects.players.attacks as a
import pygame
import settings as s


class Lucas(Player):
    def __init__(self, x, y, key_bindings, **settings):
        settings['width']=45
        settings['height']=90
        super().__init__(x, y, key_bindings, **settings)
        self.sprites = {'jump':pygame.image.load("gameobjects/players/sprites/Lucas/L_Jump.png"),
                        'walk':[pygame.image.load("gameobjects/players/sprites/Lucas/L_Walk.png"), pygame.image.load("gameobjects/players/sprites/Lucas/L_Stand.png")],
                        'stand':pygame.image.load("gameobjects/players/sprites/Lucas/L_Stand.png"),
                        'forward_tilt':pygame.image.load("gameobjects/players/sprites/Lucas/L_latk.png")}

        self.frame_count = 0
        self.time_between_frames = 10

    def process_inputs(self, event_keys, keys):
        for key in event_keys:
            if key == self.key_bindings['up'] and self.jumps_left > 1 and self.frames_in_tumble == 0:
                self.jumps_left -= 1
                self.velocity.y = 0
                self.add_force(self.jump_force)
                self.grounded_on = None
            if key == self.key_bindings['down'] and self.frames_in_tumble == 0:
                self.velocity.y = 0
                self.add_force(vec.multiply(self.jump_force, -0.5))

            if key == self.key_bindings['attack'] and self.frames_in_tumble == 0 and self.attack_collider is None:
                self.attack_collider = self.get_normal_attack()

            if key == self.key_bindings['heavy'] and self.frames_in_tumble == 0 and self.attack_collider is None:
                pass # self.attack_collider = self.get_heavy_attack()

        if keys[self.key_bindings['left']] and self.velocity.x > -self.max_runspeed and self.frames_in_tumble == 0 and self.attack_collider is None:
            if self.velocity.x > 0 and self.grounded_on:
                run_force = vec.multiply(self.run_force, -5)
            else:
                run_force = vec.multiply(self.run_force, -1)
            self.add_force(run_force)
            self.direction_facing = -1

        if keys[self.key_bindings['right']] and self.velocity.x < self.max_runspeed and self.frames_in_tumble == 0 and self.attack_collider is None:
            if self.velocity.x < 0 and self.grounded_on:
                run_force = vec.multiply(self.run_force, 5)
            else:
                run_force = self.run_force
            self.add_force(run_force)
            self.direction_facing = 1

    def get_forward_tilt_attack(self):
        offset_1 = vec.Vector2(0, -self.collider.height*0.5)
        offset_2 = vec.Vector2(2*self.collider.width, -self.collider.height*0.1)
        return a.NormalAttack(self.collider.center.x, self.collider.center.y, local_p1=offset_1, local_p2=offset_2)

    # Put all logic for normal attacks here like tilt and arial attacks
    def get_normal_attack(self):

        # Put all tilt attacks here
        if self.grounded_on:

            if self.velocity.x != 0:
                return self.get_forward_tilt_attack()

            # Neutral tilt
            else:
                return self.get_forward_tilt_attack()


        # Put all arial attacks here
        else:

            # TODO add arial attacks
            return self.get_forward_tilt_attack() # TEMPORARY

    def draw(self, screen):
        if s.DEBUG: self.collider.draw_collider(screen, s.RED)
        if self.attack_collider is not None:
            self.image = self.sprites['forward_tilt']

        # In the air
        elif not self.grounded_on:
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

        self.image = pygame.transform.scale(self.image, (90, 150))
        # Change direction of sprites
        if self.direction_facing == -1:
            self.image = pygame.transform.flip(self.image, True, False)
        screen.blit(self.image, [self.position.x-51, self.position.y-35])


