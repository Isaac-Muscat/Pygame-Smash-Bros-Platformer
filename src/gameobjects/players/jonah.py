from gameobjects.players.player import Player
import pygame

class Jonah(Player):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.framecount = 0
        self.frame1 = 10
        self.frame2 = 20

    def draw(self, screen):

        if self.position.y < 690:
            self.image = pygame.image.load("Sprites/Jonah/R/jump1.png")

        elif round(self.velocity.x, 1) != 0:
            self.framecount += 1
            if self.framecount <= self.frame1:
                self.image = pygame.image.load("Sprites/Jonah/R/walk2.png")

            elif self.frame1 <= self.framecount <= self.frame2:
                self.image = pygame.image.load("Sprites/Jonah/R/stand1.png")
                if self.framecount == self.frame2:
                    self.framecount = 0

        else:
            self.image = pygame.image.load("Sprites/Jonah/R/stand1.png")


        self.image = pygame.transform.scale(self.image, (150, 150))
        if self.direction_facing == -1:
            self.image = pygame.transform.flip(self.image, True, False)
        screen.blit(self.image, [self.position.x - 75, self.position.y - 75])
