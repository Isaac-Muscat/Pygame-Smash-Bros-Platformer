'''
Author: Isaac Muscat and Jonah D'Monte
Date: Sunday, June 13, 2021
Description: A Super Smash Bros clone using the PyGame module. The character sprites all come from real people.
'''

# Packages, Libraries, and Modules
from scenes import GameScene, MainMenu, PostGameP1, PostGameP2, CharacterSelect
import settings as s
import pygame



def main():
    '''
    This is the main function which runs the setup and the main loop

    :return: NA.
    '''
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

        # Event filtering for possible exits of the game @arrays/lists/dictionaries
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
            # Determine if the user quit the game
            if quit_attempt:
                active_scene.terminate()
            else:
                filtered_events.append(event)
        # process the inputs based on the current scene
        active_scene.process_input(filtered_events, pressed_keys)

        # Update the logic for the current scene
        active_scene.update(time)

        # Display any visuals for the current scene
        active_scene.display(screen)

        # Set the next scene (default set to itself to continue using the same scene)
        active_scene = active_scene.next

        pygame.display.flip()

        # This is used to control the framerate and provide information to the physics engine about the time since the last frame
        time = clock.tick(s.FPS)

    pygame.quit()

# Just some code to ensure the main function runs if this is run from a terminal
if __name__ == "__main__":
    main()
