
#Packages, Libraries, and Modules
import pygame
pygame.init()

#Variables
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

screen_size = (800, 600)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Duper Crash Bros")
run = True
clock = pygame.time.Clock()


#Main Loop
while run:
    #Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #Logic


    #Drawing
    screen.fill(WHITE)



    #Finally
    clock.tick(60)
    pygame.display.flip()

pygame.quit()