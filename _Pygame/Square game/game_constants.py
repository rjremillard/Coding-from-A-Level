import pygame

# Colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (211, 211, 211)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# Text
pygame.font.init()
FONT = pygame.sysfont.SysFont("Comfortaa", 20)
BIG_FONT = pygame.sysfont.SysFont("Comfortaa", 50)
START_TEXT = "Use WASD to move and space to stop\nHitting a wall causes death".split("\n")
DEATH_TEXT = "You have died".split("\n")

# Game controls
FPS = 120
SIZE = (1200, 700)
INF = 10000
KEY_VALUES = {pygame.K_w: (0, -.02), pygame.K_s: (0, .02), pygame.K_a: (-.02, 0), pygame.K_d: (.02, 0)}
