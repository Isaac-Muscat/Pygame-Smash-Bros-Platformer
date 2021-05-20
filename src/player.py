from physics.rigidbody import Rigidbody
import pygame

class Player(Rigidbody):
    def __init__(self, screen, x, y, size, mass):
        super().__init__(x, y, mass)

        self.screen = screen
        self.screen_size = screen.get_size()

        self.size = size
        self.collider = self.create_collider()

        self.sprite = 'sprite path stuff'

    def create_collider(self):
        return 0

    def draw(self):
        pass

    def update(self):
        pass