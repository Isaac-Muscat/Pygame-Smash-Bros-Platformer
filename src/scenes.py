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
        self.box1 = BoxCollider2(480, 50, 680, 100)
        self.player = Player(100, 100, 10, 10)
        self.box2 = BoxCollider2(520, 200, 590, 250)

    def process_input(self, events, pressed_keys):
        x, y = pygame.mouse.get_pos()
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 520 < x < 590 and 200 < y < 250:
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
        screen.blit(title, (480, 50))
        start = font.render("Start", False, (0, 0, 0))
        screen.blit(start, (520, 200))


class CharacterSelect(Scene):
    def __init__(self):
        super().__init__()
        self.box1 = BoxCollider2(480, 650, 700, 700)

    def process_input(self, events, pressed_keys):
        x, y = pygame.mouse.get_pos()
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 480 < x < 700 and 650 < y < 700:
                    self.switch_to_scene(GameScene())

    def update(self):
        pass

    def display(self, screen):
        screen.fill(s.PURPLE)
        self.box1.draw_collider(screen, s.WHITE)
        pygame.font.init
        font = pygame.font.SysFont("Arial", 30)
        start = font.render("Start", False, (0, 0, 0))
        screen.blit(start, (600, 650))


class GameScene(Scene):
    def __init__(self):
        super().__init__()
        self.circle = CircleCollider2(random.randint(0, s.screen_size[0]), random.randint(0, s.screen_size[1]), 10)
        x, y = pygame.mouse.get_pos()
        self.box = BoxCollider2(x, y, x + 50, y + 50)
        self.player = Player(100, 100, 10, 10)
        self.floor = BoxCollider2(0, 720, 1280, 600)
        self.sun = CircleCollider2(0, 0, 100)

    def process_input(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(self.box.collider_has_collided(self.circle))

    def update(self):
        x, y = pygame.mouse.get_pos()
        self.box.set_position(x, y)

    def display(self, screen):
        screen.fill(s.SKYBLUE)
        self.floor.draw_collider(screen, s.GREEN)
        self.sun.draw_collider(screen, s.YELLOW)
