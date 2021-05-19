import pygame

class Player(object):
    def __init__(self, screen, pos, size):
        self.screen = screen
        self.screen_size = screen.get_size()
        self.pos = pos
        self.size = size
        self.collider = self.create_collider()
        self.velocity = 0

    def create_collider(self):
        return 0

    def draw(self):
        pass

    def update(self):
        pass