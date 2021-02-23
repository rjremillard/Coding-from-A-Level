"""Constants for use in frontend.py"""

import pygame

# Colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (211, 211, 211)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# Text
pygame.font.init()  # Initialise font
FONT = pygame.sysfont.SysFont("Comfortaa", 20)  # Smaller font
BIG_FONT = pygame.sysfont.SysFont("Comfortaa", 50)  # Larger font
START_TEXT = "Use WASD to move and space to stop\nHitting a wall causes death".split("\n")  # Text displayed at start
DEATH_TEXT = "You have died".split("\n")  # Text displayed on death

# Game controls
FPS = 120  # Game ticks per second
SIZE = (1200, 700)  # Size of the game screen
INF = 10000  # A large number to act as infinity
BOUNDS_NUM = 6  # Number of randomly generated Boundaries
BOUND_MIN_SIZE = 10  # Minimum width and height of the boundaries

# Acceleration vectors per key
KEY_VALUES = {pygame.K_w: (0, -.02), pygame.K_s: (0, .02), pygame.K_a: (-.02, 0), pygame.K_d: (.02, 0)}
