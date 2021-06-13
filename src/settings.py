import pygame

# Variables

DEBUG = True
FPS = 60

# screen size, used as a scalar for graphics
s_s = (1440, 900)
h_s_s = (int(s_s[0]/2), int(s_s[1]/2))
map_multiplier = 1.5

# Key bindings for players
p1_bindings = {
    'left':  pygame.K_a,
    'right': pygame.K_d,
    'up':    pygame.K_w,
    'down':  pygame.K_s,
    'attack':pygame.K_f,
    'heavy' :pygame.K_g
}

p2_bindings = {
    'left':  pygame.K_LEFT,
    'right': pygame.K_RIGHT,
    'up':    pygame.K_UP,
    'down':  pygame.K_DOWN,
    'attack':pygame.K_n,
    'heavy' :pygame.K_m
}

# Colors
BLACK = (0, 0, 0)
GREY = (40, 40, 40)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
SKYBLUE = (135, 206, 235)
PURPLE = (120, 0, 120)
