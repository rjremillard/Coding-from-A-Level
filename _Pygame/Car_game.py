"""
Game involving controlling a player and avoiding a number of enemies

Controls:
	- W = Up
	- S = Down
	- A = Left
	- D = Right

	- Space = Stop
"""

# Imports
import pygame
import random

from typing import Tuple, List


# Constants / variables
# Colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (211, 211, 211)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

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
KEY_VALUES = {pygame.K_w: (0, -.01), pygame.K_s: (0, .01), pygame.K_a: (-.01, 0), pygame.K_d: (.01, 0)}


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
	def __init__(self, max_speed: float, colour: Tuple[int, int, int] = BLACK):
		self.speeds = [0, 0]
		self.coords = [20, 20]
		self.maxSpeed = max_speed
		self.colour = colour
		self.hit = False

	def update(self, change_x: int, change_y: int, *boundaries):
		# Sort speeds to be under max, keep to 2 dp
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
	enemyNum = 0

	def __init__(self, max_speed: float, colour: Tuple[int, int, int] = RED):
		self.maxSpeed = max_speed
		self.colour = colour
		self.coords = [1000, 600]
		self.number = Enemy.enemyNum
		Enemy.enemyNum += 1

	def update(self, player_coords: List[int], *boundaries):
		"""Will move enemy toward player, using a unit vector for the direction. Adds in some random variation too"""
		# TODO: Make avoid boundaries
		# Calculate differences in coords
		diffX, diffY = player_coords[0] - self.coords[0], player_coords[1] - self.coords[1]
		# Calculate magnitude of vector
		vectorMag = pow(pow(abs(diffX), 2) + pow(abs(diffY), 2), .5)
		# Apply magnitude to create unit vector
		try:
			changeX = (diffX / vectorMag) * self.maxSpeed * random.uniform(.5, 1.5)
		except ZeroDivisionError:
			changeX = 0

		try:
			changeY = (diffY / vectorMag) * self.maxSpeed * random.uniform(.5, 1.5)
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


# Pygame setup
pygame.init()
screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

# Boundaries
BOUNDARIES = [
	Boundary((-10, -INF), (SIZE[0]+10, -INF), (SIZE[0]+10, 0), (-10, 0)),  # Top
	Boundary((-10, SIZE[1]), (SIZE[0]+10, SIZE[1]), (SIZE[0]+10, SIZE[1]+INF), (-10, SIZE[1]+INF)),  # Bottom
	Boundary((SIZE[0]-INF, -10), (0, -10), (0, SIZE[1]+10), (SIZE[0]-INF, SIZE[1]+10)),  # Left
	Boundary((SIZE[0], -10), (SIZE[0]+INF, -10), (SIZE[0]+INF, SIZE[1]+10), (SIZE[0], SIZE[1]+10)),  # Right
	Boundary((100, 300), (300, 300), (300, 500), (100, 500)),
	Boundary((700, 100), (800, 100), (800, 500), (700, 500)),
	Boundary((100, 350), (700, 350), (700, 450), (100, 450))
]

# Player and enemies
player = Player(5)
enemies = [Enemy(1, RED), Enemy(1.5, RED), Enemy(1.3, RED)]
touches = [0 for _ in range(len(enemies))]

# Game variables
done, keypress, dead = False, False, False
keysDown = {pygame.K_w: False, pygame.K_s: False, pygame.K_a: False, pygame.K_d: False}
aliveTime = 0
while not done:
	directions = [0, 0]
	for ev in pygame.event.get():
		if ev.type == pygame.QUIT:  # Quit
			done = True

		if not dead:
			# If can move, sort key presses
			if ev.type == pygame.KEYDOWN:
				if ev.key in keysDown:
					# Enemy moves when you do
					keypress= True
					# Set key to pressed
					keysDown[ev.key] = True
					# Sort space
				if ev.key == pygame.K_SPACE:
					player.speeds = [0, 0]

			elif ev.type == pygame.KEYUP:
				if ev.key in keysDown:
					# Key no longer pressed
					keysDown[ev.key] = False

	if not dead:
		# Add to alive time
		aliveTime += 1

		# Sort keys still pressed
		for key in keysDown:
			if keysDown[key]:
				directions[0] += KEY_VALUES[key][0]
				directions[1] += KEY_VALUES[key][1]

		# Clean screen to draw
		screen.fill(GREY)

		# Update player and enemies
		player.update(*directions, *BOUNDARIES)
		pygame.draw.rect(screen, player.colour, (player.coords[0]-10, player.coords[1]-10, 20, 20))

		for enemy in enemies:
			if any(keysDown.values()):
				enemy.update(player.coords, *BOUNDARIES)
			pygame.draw.rect(screen, enemy.colour, (enemy.coords[0]-10, enemy.coords[1]-10, 20, 20))

			# Check if player has been hit
			if player.coords[0]-2 < enemy.coords[0] < player.coords[0]+22\
					and player.coords[1]-2 < enemy.coords[1] < player.coords[1]+22:
				touches[enemy.number] += 1
			else:
				touches[enemy.number] = 0

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

		# Death timer
		deathText = FONT.render(f"Death timer: {round(max(touches)/FPS, 2)}s", 3, BLACK)
		screen.blit(deathText, (10, 46))

		# Alive timer
		aliveText = FONT.render(f"Alive timer: {round(aliveTime/FPS, 2)}s", 4, BLACK)
		screen.blit(aliveText, (10, 58))

	# Draw boundaries
	for bound in BOUNDARIES:
		pygame.draw.polygon(screen, bound.colour, bound.pointList)

	# Draw death text now (over boundaries), die after one second of touch
	if max(touches) >= FPS:
		dead = True
		line = BIG_FONT.render("You have died", -10, BLACK)
		screen.blit(line, (SIZE[0]/2 - 60, SIZE[1]/2 - 20))

	# Sort screen
	pygame.display.flip()
	clock.tick(FPS)

pygame.quit()
