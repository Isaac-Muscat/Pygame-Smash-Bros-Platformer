import random

import pygame

import settings as s
from gameobjects import Player, Ground
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
    def __init__(self):
        super().__init__()
        self.player = Player()
        self.floor = Ground(s.s_s[0] * 0.2, s.s_s[1] * 0.75, s.s_s[0] * 0.80, s.s_s[1] * 0.7)

        #BACKGROUND
        self.pillar = BoxCollider2(s.s_s[0] * 0.3, s.s_s[1] * 0.7, s.s_s[0] * 0.7, s.s_s[1]+200).set_active(False)
        self.sun = CircleCollider2(0, 0, 100).set_active(False)

    def process_input(self, events, keys):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and self.player.jumps_left>1 and self.player.frames_in_tumble==0:
                    self.player.jumps_left -= 1
                    self.player.velocity.y = 0
                    self.player.add_force(self.player.jump_force)
        if keys[pygame.K_a]:
            #self.player.add_force(vec.multiply(self.player.run_force, -1))
            self.player.velocity.x = -self.player.run_force.x
        elif keys[pygame.K_d]:
            #self.player.add_force(self.player.run_force)
            self.player.velocity.x = self.player.run_force.x
        else:
            self.player.velocity.x = 0


    def update(self, clock):
        if self.floor.player_collided_from_top(self.player):
            self.player.jumps_left = self.player.jumps
            self.player.velocity.y = 0
            self.player.position.y = self.floor.p1.y-self.player.collider.height

        else:
            self.player.add_force(self.player.gravity)
        self.player.update(clock)


    def display(self, screen):
        screen.fill(s.SKYBLUE)
        self.sun.draw_collider(screen, s.YELLOW)
        self.pillar.draw_collider(screen, s.GREY)

        self.floor.draw_collider(screen, s.GREEN)
        self.player.draw(screen)
