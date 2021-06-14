from gameobjects.players.player import Player
import physics.vector2 as vec
import gameobjects.players.attacks as a
import pygame
import settings as s


class Jonah(Player):
    def __init__(self, x, y, key_bindings, **settings):
        # Hitbox dimensions
        settings['width']=45
        settings['height']=90
        settings["gravity_coef"] = 0.4
        settings["max_fallspeed"] = 1.5
        settings["jump_force"] = vec.Vector2(0, -15)
        super().__init__(x, y, key_bindings, **settings)

        self.sprites = {'jump':pygame.image.load("gameobjects/players/sprites/Jonah/jump1.png"),
                        'walk':[pygame.image.load("gameobjects/players/sprites/Jonah/walk2.png"), pygame.image.load("gameobjects/players/sprites/Jonah/stand1.png")],
                        'stand':pygame.image.load("gameobjects/players/sprites/Jonah/stand1.png"),
                        'forward_tilt':pygame.image.load("gameobjects/players/sprites/Jonah/normalAttacks/forward_tilt.png"),
                        'forward_special':pygame.image.load("gameobjects/players/sprites/Jonah/heavyAttacks/vine.png")}

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
                offset_1 = vec.Vector2(0, +self.collider.height * 0.7)
                offset_2 = vec.Vector2(6 * self.collider.width, +self.collider.height * 0.1)
                self.attack_collider = a.VineAttack(self.collider.center.x, self.collider.center.y, local_p1=offset_1, local_p2=offset_2)

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
        if self.attack_collider is not None and type(self.attack_collider) is a.NormalAttack:
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

        self.image = pygame.transform.scale(self.image, (150, 150))
        # Change direction of sprites
        if self.direction_facing == -1:
            self.image = pygame.transform.flip(self.image, True, False)
        screen.blit(self.image, [self.position.x-51, self.position.y-35])

        if self.attack_collider is not None and type(self.attack_collider) is a.VineAttack:
            attack = self.sprites['forward_special']
            attack = pygame.transform.scale(attack, (300, 50))
            if self.direction_facing == -1:
                attack = pygame.transform.flip(attack, True, False)
                screen.blit(attack, [self.position.x - 300, self.position.y+75])
            else:
                screen.blit(attack, [self.position.x+50, self.position.y+75])



