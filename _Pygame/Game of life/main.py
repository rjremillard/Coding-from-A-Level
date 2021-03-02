"""https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life"""

import pygame

import numpy as np


# Constants
SIZE = (1200, 700)

# Make grid
grid = []
for _ in range(0, SIZE[1]+100, 10):
	grid.append([False for _ in range(0, SIZE[0]+100, 10)])

grid[50][50] = True
grid[51][50] = True
grid[50][51] = True

# Pygame setup
pygame.init()
screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

# Game loop
game = True
while game:
	for ev in pygame.event.get():
		if ev.type == pygame.KEYDOWN:
			if ev.key == pygame.QUIT:
				game = False

	screen.fill((255, 255, 255))

	for row in range(50, SIZE[1]-50, 10):
		for column in range(50, SIZE[0]-50, 10):
			neighbours = sum([
				grid[row-1][column-1], grid[row-1][column], grid[row-1][column+1],
				grid[row][column-1], grid[row][column+1],
				grid[row+1][column-1], grid[row+1][column], grid[row+1][column+1]
			])

			if grid[row][column]:
				colour = (0, 255, 0)
				if neighbours < 2 or neighbours > 3:
					grid[row][column] = False
			else:
				colour = (255, 255, 255)
				if neighbours == 3:
					grid[row][column] = True

			pygame.draw.rect(screen, colour, [row, column, 10, 10])

	clock.tick(2)
