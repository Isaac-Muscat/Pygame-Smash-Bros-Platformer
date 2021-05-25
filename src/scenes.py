import random

import pygame

import settings as s
from gameobjects import Player
from physics.collider2 import CircleCollider2, BoxCollider2


class Scene(object):
    def __init__(self):
        self.next = self

    def process_input(self, events, pressed_keys):
        print("You didn't override this in the child class.")

    def update(self):
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

    def update(self):
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

    def update(self):
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
        self.player = Player(100, 100, 10, 10)
        self.floor = BoxCollider2(0, 720, 1280, 600)
        self.sun = CircleCollider2(0, 0, 100).set_active(False)

    def process_input(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass

    def update(self):
        pass

    def display(self, screen):
        screen.fill(s.SKYBLUE)
        self.floor.draw_collider(screen, s.GREEN)
        self.sun.draw_collider(screen, s.YELLOW)
