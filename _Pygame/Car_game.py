"""
Game involving driving a car, if it hits the wall it dies

Controls:
	- W = Up
	- S = Down
	- A = Left
	- D = Right

	- Space = Stop
"""

# Imports
import pygame
import numpy

from typing import Tuple, List


# Constants / variables
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (211, 211, 211)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

pygame.font.init()
FONT = pygame.sysfont.SysFont("Comfortaa", 20)
BIG_FONT = pygame.sysfont.SysFont("Comfortaa", 50)
START_TEXT = "Use WASD to move and space to stop\nHitting a wall causes death".split("\n")
DEATH_TEXT = "You have died".split("\n")

FPS = 120
SIZE = (1200, 700)
INF = 10000
KEY_VALUES = {"w": -.01, "s": .01, "a": -.01, "d": .01}


# Boundary class
class Boundary:
	def __init__(self, *points: Tuple[int, int], colour: Tuple[int, int, int] = BLUE):
		""":param points: 2-dimensional array of coords of 4 vertices, from TL clockwise"""
		if len(points) != 4:
			raise Warning("Boundaries require 4 points to work properly")

		self.pointList = points
		self.xRange = (points[0][0], points[1][0])
		self.yRange = (points[0][1], points[2][1])
		self.colour = colour

	def inBound(self, x: float, y: float) -> bool:
		"""Calculate if certain coordinates are bound by the rectangle"""
		if self.xRange[0] < x < self.xRange[1] and self.yRange[0] < y < self.yRange[1]:
			return True
		return False


# Player class
class Player:
	def __init__(self, max_speed: int, colour: Tuple[int, int, int] = BLACK):
		self.speeds = [0, 0]
		self.coords = [20, 20]
		self.maxSpeed = max_speed
		self.colour = colour

	def update(self, change_x: int, change_y: int, *boundaries):
		# Sort speeds to be under max
		self.speeds[0] = round(self.speeds[0] + change_x, 2)
		if self.speeds[0] > self.maxSpeed:
			self.speeds[0] = self.maxSpeed

		self.speeds[1] = round(self.speeds[1] + change_y, 2)
		if self.speeds[1] > self.maxSpeed:
			self.speeds[1] = self.maxSpeed

		# Apply speeds to coords
		tmpX = self.coords[0] + self.speeds[0]
		tmpY = self.coords[1] + self.speeds[1]

		# Check for collisions
		for boundary in boundaries:
			if boundary.inBound(tmpX, tmpY):
				# Collision
				self.speeds = [0, 0]
				break
		else:
			# No collisions
			self.coords = [round(tmpX, 2), round(tmpY, 2)]


class Enemy:
	def __init__(self, max_speed: int, colour: Tuple[int, int, int] = RED):
		self.maxSpeed = max_speed
		self.colour = colour
		self.coords = [1000, 600]

	def update(self, player_coords: List[int], *boundaries):
		"""Will move enemy toward player, using a unit vector for the direction"""
		# TODO: Make avoid boundaries
		# Calculate vector
		diffX, diffY = player_coords[0] - self.coords[0], player_coords[1] - self.coords[1]
		vectorMag = pow(pow(abs(diffX), 2) + pow(abs(diffY), 2), .5)
		try:
			changeX = (diffX / vectorMag) * self.maxSpeed
		except ZeroDivisionError:
			changeX = 0

		try:
			changeY = (diffY / vectorMag) * self.maxSpeed
		except ZeroDivisionError:
			changeY = 0

		# Apply directions
		tmpX = self.coords[0] + changeX
		tmpY = self.coords[1] + changeY

		# Check for collisions
		for boundary in boundaries:
			if boundary.inBound(tmpX, tmpY):
				# Collision
				break
		else:
			# No collisions
			self.coords = [round(tmpX, 2), round(tmpY, 2)]


# Pygame loop
pygame.init()
screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

# Game variables
BOUNDARIES = [
	Boundary((-10, -INF), (SIZE[0]+10, -INF), (SIZE[0]+10, 0), (-10, 0)),  # Top
	Boundary((-10, SIZE[1]), (SIZE[0]+10, SIZE[1]), (SIZE[0]+10, SIZE[1]+INF), (-10, SIZE[1]+INF)),  # Bottom
	Boundary((SIZE[0]-INF, -10), (0, -10), (0, SIZE[1]+10), (SIZE[0]-INF, SIZE[1]+10)),  # Left
	Boundary((SIZE[0], -10), (SIZE[0]+INF, -10), (SIZE[0]+INF, SIZE[1]+10), (SIZE[0], SIZE[1]+10)),  # Right
	Boundary((100, 300), (300, 300), (300, 500), (100, 500)),
	Boundary((700, 100), (800, 100), (800, 500), (700, 500)),
	Boundary((100, 350), (700, 350), (700, 450), (100, 450))
]

player = Player(5)
enemies = [Enemy(1, RED)]

done, keypress, dead = False, False, False
keysDown = {"w": False, "s": False, "a": False, "d": False}
while not done:
	enemyMove = False
	changeX, changeY = 0, 0
	for ev in pygame.event.get():
		if ev.type == pygame.QUIT:  # Quit
			done = True

		if not dead:
			if ev.type == pygame.KEYDOWN:  # Keypress
				keypress, enemyMove = True, True
				for key in "wasd":
					if eval(f"ev.key == pygame.K_{key}"):
						keysDown[key] = True
				if ev.key == pygame.K_SPACE:
					player.speeds = [0, 0]

			elif ev.type == pygame.KEYUP:
				for key in "wasd":
					if eval(f"ev.key == pygame.K_{key}"):
						keysDown[key] = False

	if not dead:
		# Sort key presses
		for key in "ws":
			if keysDown[key]:
				changeY = KEY_VALUES[key]

		for key in "ad":
			if keysDown[key]:
				changeX = KEY_VALUES[key]

		screen.fill(GREY)

		# Update player and enemy
		player.update(changeX, changeY, *BOUNDARIES)
		pygame.draw.rect(screen, player.colour, (player.coords[0]-10, player.coords[1]-10, 20, 20))

		for enemy in enemies:
			enemy.update(player.coords, *BOUNDARIES)
			pygame.draw.rect(screen, enemy.colour, (enemy.coords[0]-10, enemy.coords[1]-10, 20, 20))

			# Check if player has been hit
			if player.coords[0]-2 < enemy.coords[0] < player.coords[0]+22\
					and player.coords[1]-2 < enemy.coords[1] < player.coords[1]+22:
				dead = True
				player.speeds = [0, 0]

	# Displaying text
	if not keypress:
		# Start text
		for line, n in zip(START_TEXT, range(len(START_TEXT))):
			line = FONT.render(line, -n, BLACK)
			screen.blit(line, (20, 20 + 12*n))
	else:
		# Helpful text
		speedXText = FONT.render(f"Speed x: {player.speeds[0]}", 0, BLACK)
		speedYText = FONT.render(f"Speed y: {-1 * player.speeds[1]}", 1, BLACK)
		coordsText = FONT.render(f"Coords:  {player.coords[0]}, {player.coords[1]}", 2, BLACK)

		screen.blit(speedXText, (10, 10))
		screen.blit(speedYText, (10, 22))
		screen.blit(coordsText, (10, 34))

	# Draw boundaries
	for bound in BOUNDARIES:
		pygame.draw.polygon(screen, bound.colour, bound.pointList)

	# Draw death text now (over boundaries)
	if dead:
		line = BIG_FONT.render("You have died", -10, BLACK)
		screen.blit(line, (SIZE[0]/2 - 60, SIZE[1]/2 - 20))

	# Sort screen
	pygame.display.flip()
	clock.tick(FPS)

pygame.quit()
