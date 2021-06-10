import math

import pygame

import settings as s
from gameobjects.obstacles import platform, wall
import gameobjects.players.jonah as j
import gameobjects.players.isaac as i
import gameobjects.players.lucas as l
import gameobjects.players.arend as ar
from physics.collider2 import CircleCollider2, BoxCollider2
import physics.vector2 as vec



class Scene(object):
    def __init__(self):
        self.next = self

    def process_input(self, events, pressed_keys):
        print("You didn't override this in the child class.")

    def update(self, clock):
        print("You didn't override this in the child class.")

    def display(self, screen):
        print("You didn't override this in the child class.")

    def switch_to_scene(self, next_scene):
        self.next = next_scene

    def terminate(self):
        self.switch_to_scene(None)


class MainMenu(Scene):
    def __init__(self):
        super().__init__()
        self.box1 = BoxCollider2(440, 50, 720, 100).set_active(False)
        self.box2 = BoxCollider2(520, 200, 590, 250)

    def process_input(self, events, pressed_keys):
        x, y = pygame.mouse.get_pos()
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.box2.point_has_collided(x, y):
                    self.switch_to_scene(CharacterSelect())

    def update(self, clock):
        pass

    def display(self, screen):
        screen.fill(s.BLUE)
        self.box1.draw_collider(screen, s.WHITE)
        self.box2.draw_collider(screen, s.RED)
        pygame.font.init()
        font = pygame.font.SysFont("Arial", 30)
        title = font.render("Duper Crash Bros", False, (0, 0, 0))
        center = title.get_rect(center=(self.box1.center.x, self.box1.center.y))
        screen.blit(title, center)
        start = font.render("Start", False, (0, 0, 0))
        center = start.get_rect(center=(self.box2.center.x, self.box2.center.y))
        screen.blit(start, center)


class CharacterSelect(Scene):
    def __init__(self):
        super().__init__()
        self.box1 = BoxCollider2(480, 650, 700, 700)

    def process_input(self, events, pressed_keys):
        x, y = pygame.mouse.get_pos()
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.box1.point_has_collided(x, y):
                    self.switch_to_scene(GameScene())

    def update(self, clock):
        pass

    def display(self, screen):
        screen.fill(s.PURPLE)
        self.box1.draw_collider(screen, s.WHITE)
        pygame.font.init()
        font = pygame.font.SysFont("Arial", 30)
        start = font.render("Start", False, (0, 0, 0))
        center = start.get_rect(center=(self.box1.center.x, self.box1.center.y))
        screen.blit(start, center)


class GameScene(Scene):
    # TODO Must add a list of players and change organization of functions into individual player classes
    def __init__(self):
        super().__init__()
        self.percent_font = pygame.font.SysFont("Arial", 100)
        self.map_s = (int(s.s_s[0] * s.map_multiplier), int(s.s_s[1] * s.map_multiplier))
        self.offset = ((self.map_s[0] - s.s_s[0]) / 2, (self.map_s[1] - s.s_s[1]) / 2)
        self.buffer = pygame.surface.Surface(self.map_s)

        self.players = [ar.Arend(self.map_s[0] * 0.4, self.map_s[1] * 0.1, s.p1_bindings),
                        l.Lucas(self.map_s[0] * 0.6, self.map_s[1] * 0.1, s.p2_bindings, direction_facing=-1)]

        self.obstacles = [
            platform.Platform(self.map_s[0] * 0.3, self.map_s[1] * 0.6, self.map_s[0] * 0.7, self.map_s[1] * 0.55,
                              s.GREEN),
            wall.Wall(self.map_s[0] * 0.31, self.map_s[1] * 0.6, self.map_s[0] * 0.69, self.map_s[1], s.GREY)]

        # BACKGROUND
        self.sun = CircleCollider2(self.map_s[0] / 2, self.map_s[1] * 0.2 / 2, 100).set_active(False)

    def process_input(self, events, keys):
        event_keys = []
        for event in events:
            if event.type == pygame.KEYDOWN:
                event_keys.append(event.key)
        for player in self.players:
            player.process_inputs(event_keys, keys)

    def update(self, time):
        for player in self.players:

            # Handle player attacks
            for player_2 in self.players:
                attack = player.attack_collider
                if player is not player_2 and attack is not None and attack.active is True and \
                        attack.collider_has_collided(player_2.collider) and \
                        attack.post_lag < attack.total_lag < \
                        attack.peri_lag + attack.post_lag:

                    player_2.velocity.multiply(0)
                    force = vec.multiply(attack.knockback_direction,
                                         attack.knockback_multiplier * (1 + player_2.damage_percentage))
                    force.x *= player.direction_facing
                    player_2.add_force(force)
                    player_2.damage_percentage += player.attack_collider.percent_damage
                    player_2.frames_in_tumble = player.attack_collider.stun_duration
                    attack.set_active(False)
                    # Move attacking player to end of list for drawing overtop other player
                    self.players.append(self.players.pop(self.players.index(player)))

            # Handle obstacle collision
            for obstacle in self.obstacles:
                if obstacle.player_collided_from_top(player):
                    player.jumps_left = player.jumps
                    player.velocity.y = 0
                    player.position.y = obstacle.p1.y - player.collider.height
                    player.grounded_on = obstacle
                elif player.grounded_on == obstacle and obstacle.player_has_fallen_off(player):
                    player.grounded_on = None
                elif obstacle.player_collided_from_bottom(player):
                    player.velocity.y = 0
                    player.position.y = obstacle.p2.y
                elif obstacle.player_collided_from_left(player):
                    player.velocity.x = 0
                    player.position.x = obstacle.p1.x-player.collider.width
                elif obstacle.player_collided_from_right(player):
                    player.velocity.x = 0
                    player.position.x = obstacle.p2.x+1

            if player.velocity.y < 0 and player.grounded_on is not None:
                player.grounded_on = None
            if player.velocity.y < player.max_fallspeed and player.grounded_on is None:
                player.add_gravity(player.gravity_coef)

            player.add_friction(player.friction_coef)
            player.add_drag(player.drag_coef)
            player.update(time)

        # Uncomment for players to face each other disregarding input
        '''
        if self.players[0].position.x < self.players[1].position.x:
            self.players[0].direction_facing = 1
            self.players[1].direction_facing = -1
        elif self.players[0].position.x > self.players[1].position.x:
            self.players[0].direction_facing = -1
            self.players[1].direction_facing = 1
        #'''

    def display(self, screen):
        # Display background
        self.buffer.fill(s.SKYBLUE)
        self.sun.draw_collider(self.buffer, s.YELLOW)

        # Display physics objects
        for obstacle in self.obstacles:
            obstacle.draw_collider(self.buffer)
        for player in self.players:
            player.draw(self.buffer)
            if player.attack_collider is not None and s.DEBUG:
                player.attack_collider.draw_collider(self.buffer, s.BLACK)

        # Handle translating the camera view
        dist_x = (self.players[0].collider.center.x + self.players[1].collider.center.x) / 2
        dist_y = (self.players[0].collider.center.y + self.players[1].collider.center.y) / 2
        translation = vec.Vector2(
            vec.clamp((self.map_s[0] / 2) - dist_x, (s.s_s[0] - self.map_s[0]) / 2, (self.map_s[0] - s.s_s[0]) / 2),
            vec.clamp((self.map_s[1] / 2) - dist_y, (s.s_s[1] - self.map_s[1]) / 2, (self.map_s[1] - s.s_s[1]) / 2))

        screen.blit(pygame.transform.scale(self.buffer, self.map_s),
                    (translation.x - self.offset[0], translation.y - self.offset[1]))

        # Display health
        for i in range(len(self.players)):
            stats = self.percent_font.render(str(round(self.players[i].damage_percentage * 100)) + '%', False,
                                             (0, 0, 0))
            center = stats.get_rect(center=(self.offset[0] + self.map_s[0] * 0.3 * i, self.map_s[1] * 0.5))
            screen.blit(stats, center)
