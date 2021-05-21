import random

import pygame

from src import settings as s
from src.gameobjects import Player
from src.physics.collider2 import CircleCollider2, BoxCollider2


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

    def process_input(self, events, pressed_keys):
        pass

    def update(self):
        pass

    def display(self, screen):
        pass

class GameScene(Scene):
    def __init__(self):
        super().__init__()
        self.circle = CircleCollider2(random.randint(0, s.screen_size[0]), random.randint(0, s.screen_size[1]), 10)
        x, y = pygame.mouse.get_pos()
        self.box = BoxCollider2(x, y, x + 50, y + 50)
        self.player = Player(100, 100, 10, 10)

    def process_input(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(self.box.collider_has_collided(self.circle))

    def update(self):
        x, y = pygame.mouse.get_pos()
        self.box.set_position(x, y)

    def display(self, screen):
        screen.fill(s.WHITE)
        self.circle.draw_collider(screen, s.BLACK)
        self.box.draw_collider(screen, s.GREEN)