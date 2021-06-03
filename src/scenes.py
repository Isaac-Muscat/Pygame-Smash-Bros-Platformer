import math

import pygame

import settings as s
from gameobjects.obstacles import platform, wall
import gameobjects.players.jonah as j
import gameobjects.players.isaac as i
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
        map_multiplier = 1.5
        self.map_s = (int(s.s_s[0] * map_multiplier), int(s.s_s[1] * map_multiplier))
        self.offset = ((self.map_s[0] - s.s_s[0]) / 2, (self.map_s[1] - s.s_s[1]) / 2)
        self.buffer = pygame.surface.Surface(self.map_s)

        self.players = [j.Jonah(self.map_s[0] * 0.4, self.map_s[1] * 0.3),
                        i.Isaac(self.map_s[0] * 0.6, self.map_s[1] * 0.3)]

        self.obstacles = [platform.Platform(self.map_s[0] * 0.3, self.map_s[1] * 0.6, self.map_s[0] * 0.7, self.map_s[1] * 0.55, s.GREEN),
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
            for obstacle in self.obstacles:
                obstacle.handle_player_collision(player, time)

        # Uncomment for players to face each other disregarding input
        '''if self.players[0].position.x < self.players[1].position.x:
            self.players[0].direction_facing = 1
            self.players[1].direction_facing = -1
        elif self.players[0].position.x > self.players[1].position.x:
            self.players[0].direction_facing = -1
            self.players[1].direction_facing = 1'''

    def display(self, screen):
        # Display background
        self.buffer.fill(s.SKYBLUE)
        self.sun.draw_collider(self.buffer, s.YELLOW)

        # Display physics objects
        for obstacle in self.obstacles:
            obstacle.draw_collider(self.buffer)
        for player in self.players:
            player.draw(self.buffer)

        # Handle translating the camera view
        dist_x = (self.players[0].collider.center.x + self.players[1].collider.center.x) / 2
        dist_y = (self.players[0].collider.center.y + self.players[1].collider.center.y) / 2
        translation = vec.Vector2(
            vec.clamp((self.map_s[0] / 2) - dist_x, (s.s_s[0] - self.map_s[0]) / 2, (self.map_s[0] - s.s_s[0]) / 2),
            vec.clamp((self.map_s[1] / 2) - dist_y, (s.s_s[1] - self.map_s[1]) / 2, (self.map_s[1] - s.s_s[1]) / 2))
        screen.blit(pygame.transform.scale(self.buffer, self.map_s),
                    (translation.x - self.offset[0], translation.y - self.offset[1]))
