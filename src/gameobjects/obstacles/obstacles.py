from src.physics.collider2 import BoxCollider2

class Obstacle(BoxCollider2):
    def __init__(self, x1, y1, x2, y2):
        super().__init__(x1, y1, x2, y2)

    def player_collided_from_top(self, player):
        if player.velocity.y > 0 and not player.collider.p2.x < self.p1.x and not player.collider.p1.x > self.p2.x and self.p1.y <= player.collider.p2.y:
            if player.prev_collider.p2.y <= self.p1.y and (self.p1.x < player.prev_collider.p1.x < self.p2.x or self.p1.x < player.prev_collider.p2.x < self.p2.x):
                return True
        return False

    # TODO use prev_collider
    def player_collided_from_bottom(self, player):
        if player.velocity.y<0 and not player.collider.p2.x < self.p1.x and not player.collider.p1.x > self.p2.x and player.collider.p1.y > self.p2.y > player.collider.p2.y:
            return True
        return False

    # TODO use prev_collider
    def player_collided_from_left(self, player):
        if player.velocity.x>0 and player.collider.p2.x > self.p1.x > player.collider.p1.x and self.p1.y:
            return True
        return False

    # TODO use prev_collider
    def player_collided_from_right(self, player):
        if player.velocity.x<0 and not player.collider.p2.x < self.p1.x and not player.collider.p1.x > self.p2.x and player.collider.p1.y < self.p1.y < player.collider.p2.y:
            return True
        return False