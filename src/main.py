# Author: Isaac Muscat and Jonah D'Monte
# Date: Sunday, June 13, 2021
# Description: A Super Smash Bros clone using the PyGame module

# Packages, Libraries, and Modules
from scenes import GameScene, MainMenu, PostGameP1, PostGameP2, CharacterSelect
import settings as s
import pygame


def main():
    pygame.init()

    # SETUP
    screen = pygame.display.set_mode(s.s_s)
    pygame.display.set_caption("Duper Crash Bros")
    clock = pygame.time.Clock()
    time = clock.tick(s.FPS)
    active_scene = MainMenu()

    # UPDATE - Main Loop
    while active_scene is not None:
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
        active_scene.update(time)
        active_scene.display(screen)


        active_scene = active_scene.next

        pygame.display.flip()
        time = clock.tick(s.FPS)

    pygame.quit()


if __name__ == "__main__":
    main()
