from physics.rigidbody import Rigidbody


class Player(Rigidbody):
    def __init__(self, x, y, size, mass):
        super().__init__(x, y, mass)

        self.size = size
        self.collider = self.create_collider()

        self.sprite = 'sprite path stuff'

    def create_collider(self):
        return 0

    def draw(self, screen):
        pass

    def update(self):
        pass