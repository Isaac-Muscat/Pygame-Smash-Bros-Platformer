import pygame
from physics.collider2 import BoxCollider2


class Obstacle(BoxCollider2):
    '''
    Describes a generic platform or immovable aspects of the environment.
    '''
    def __init__(self, x1, y1, x2, y2, color):
        super().__init__(x1, y1, x2, y2)
        self.color = color

    def player_has_fallen_off(self, player):
        '''
        Determines if the player has fallen off the obstacle.
        '''
        if player.collider.p1.x > self.p2.x or player.collider.p2.x < self.p1.x:
            return True
        else:
            return False

    # Next 4 functions used to prevent the player from passing though the obstacle
    def player_collided_from_top(self, player):
        if player.velocity.y > 0 and not player.collider.p2.x < self.p1.x and not player.collider.p1.x > self.p2.x and self.p1.y <= player.collider.p2.y:
            if player.prev_collider.p2.y <= self.p1.y and (
                    self.p1.x < player.prev_collider.p1.x < self.p2.x or self.p1.x < player.prev_collider.p2.x < self.p2.x):
                return True
        return False

    def player_collided_from_bottom(self, player):
        if player.velocity.y < 0 and not player.collider.p2.x < self.p1.x and not player.collider.p1.x > self.p2.x and self.p2.y >= player.collider.p1.y:
            if player.prev_collider.p1.y >= self.p2.y and (
                    self.p1.x < player.prev_collider.p1.x < self.p2.x or self.p1.x < player.prev_collider.p2.x < self.p2.x):
                return True
        return False

    def player_collided_from_left(self, player):
        if player.velocity.x > 0 and player.collider.p1.x < self.p1.x < player.collider.p2.x and \
                (self.p1.y < player.collider.p1.y < self.p2.y or self.p1.y < player.collider.p2.y < self.p2.y or
                player.collider.p1.y < self.p1.y < player.collider.p2.y):
            if not player.prev_collider.p2.x > self.p1.x > player.prev_collider.p1.x:
                return True
        return False

    def player_collided_from_right(self, player):
        if player.velocity.x < 0 and player.collider.p1.x < self.p2.x < player.collider.p2.x and \
                (self.p1.y < player.collider.p1.y < self.p2.y or self.p1.y < player.collider.p2.y < self.p2.y or
                 player.collider.p1.y < self.p1.y < player.collider.p2.y):
            if not player.prev_collider.p1.x < self.p2.x < player.prev_collider.p2.x:
                return True
        return False

    def draw_collider(self, screen):
        pygame.draw.rect(screen, self.color,
                         pygame.Rect(self.p1.x, self.p1.y, self.p2.x - self.p1.x, self.p2.y - self.p1.y))
