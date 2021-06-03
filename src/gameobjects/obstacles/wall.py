import pygame

from obstacles import Obstacle


class Wall(Obstacle):
    def __init__(self, x1, y1, x2, y2, color):
        super().__init__(int(x1), int(y1), int(x2), int(y2), color)

    def handle_player_collision(self, player, time):
        pass

    def draw_collider(self, screen):
        pygame.draw.rect(screen, self.color,
                         pygame.Rect(self.p1.x, self.p1.y, self.p2.x - self.p1.x, self.p2.y - self.p1.y))