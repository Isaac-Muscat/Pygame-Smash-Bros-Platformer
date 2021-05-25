#Packages, Libraries, and Modules
from scenes import GameScene, MainMenu
import settings as s
import pygame
pygame.init()

#SETUP
screen = pygame.display.set_mode(s.screen_size)
pygame.display.set_caption("Duper Crash Bros")
clock = pygame.time.Clock()
active_scene = MainMenu()

#UPDATE - Main Loop
while active_scene!=None:
    pressed_keys = pygame.key.get_pressed()

    # Event filtering
    filtered_events = []
    for event in pygame.event.get():
        quit_attempt = False
        if event.type == pygame.QUIT:
            quit_attempt = True
        elif event.type == pygame.KEYDOWN:
            alt_pressed = pressed_keys[pygame.K_LALT] or \
                          pressed_keys[pygame.K_RALT]
            if event.key == pygame.K_ESCAPE:
                quit_attempt = True
            elif event.key == pygame.K_F4 and alt_pressed:
                quit_attempt = True

        if quit_attempt:
            active_scene.terminate()
        else:
            filtered_events.append(event)

    active_scene.process_input(filtered_events, pressed_keys)
    active_scene.update()
    active_scene.display(screen)

    active_scene = active_scene.next

    pygame.display.flip()
    clock.tick(60)

pygame.quit()