
#Packages, Libraries, and Modules
from physics.collider2 import BoxCollider2
from physics.collider2 import CircleCollider2
from player import Player

import random

import pygame
pygame.init()

#Variables
screen_size = (800, 600)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

DEBUG = True
run = True



#SETUP
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Duper Crash Bros")
clock = pygame.time.Clock()

circle = CircleCollider2(random.randint(0, screen_size[0]), random.randint(0, screen_size[1]),10)
x, y = pygame.mouse.get_pos()
box = BoxCollider2(x, y, x+50, y+50)
player = Player(screen, 100, 100, 10, 10)


#UPDATE - Main Loop
while run:
    #Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(box.collider_has_collided(circle))

    #Logic
    x, y = pygame.mouse.get_pos()
    box.set_position(x, y)

    #Drawing
    screen.fill(WHITE)
    circle.draw_collider(screen, BLACK)
    box.draw_collider(screen, GREEN)


    #Finally
    clock.tick(60)
    pygame.display.flip()

pygame.quit()