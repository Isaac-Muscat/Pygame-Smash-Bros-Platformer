from gameobjects.players.player import Player
import settings as s

class Isaac(Player):
    def __init__(self, x, y):
        super().__init__(x, y)

    def draw(self, screen):
        # TODO sprite stuff here
        self.collider.draw_collider(screen, s.BLUE)