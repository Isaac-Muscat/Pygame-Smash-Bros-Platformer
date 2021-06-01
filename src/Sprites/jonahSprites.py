import pygame

class Jonah(pygame.sprite.Sprite):
    def __init__(self, width, height, posx, posy):
        super().__init__()

        self.image = pygame.image.load("Sprites/Jonah/R/stand1.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = posx
        self.rect.y = posy

