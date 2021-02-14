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

from typing import Tuple


# Constants / variables
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (211, 211, 211)
RED = (255, 0, 0)

pygame.font.init()
FONT = pygame.sysfont.SysFont("Comfortaa", 20)
START_TEXT = "Use WASD to move\nHitting a wall will stop all movement,\nas does the space bar".split("\n")

FPS = 120
SIZE = (1200, 700)
GAME_SIZE = (SIZE[0]-20, SIZE[1]-20)
INF = 10000


# Boundary class
class Boundary:
	def __init__(self, *points: Tuple[int, int], colour: Tuple[int, int, int] = RED):
		""":param points: 2-dimensional array of coords of 4 vertices"""
		self.pointList = points
		self.xRange = numpy.arange(points[0][0], points[1][0])
		self.yRange = numpy.arange(points[0][1], points[2][1])
		self.colour = colour

	def inBound(self, x: float, y: float) -> bool:
		"""Calculate if certain coordinates are bound by the inequality"""
		if x in self.xRange and y in self.yRange:
			return True
		return False

	@staticmethod
	def toInt(a: Tuple[float, ...]) -> Tuple[int, ...]:
		return tuple(map(int, a))


# Player class
class Player:
	def __init__(self, colour: Tuple[int, int, int] = BLACK):
		self.speeds = [0, 0]
		self.coords = [10, 10]
		self.colour = colour

	def update(self, change_x: int, change_y: int, *boundaries):
		# Apply changes
		xTmp = self.coords[0] + self.speeds[0] + change_x
		yTmp = self.coords[1] + self.speeds[1] + change_y

		# Check boundaries
		# TODO: Avoid passing bounds as coords are TL
		for bound in boundaries:
			if bound.inBound(xTmp, yTmp):
				self.speeds = [0, 0]
				break
		else:  # All is good
			# Sort speeds
			self.speeds[0] += change_x
			self.speeds[1] += change_y

			self.coords[0] = xTmp
			self.coords[1] = yTmp


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
player = Player()

done, keypress = False, False
while not done:
	changeX, changeY = 0, 0
	for ev in pygame.event.get():
		if ev.type == pygame.QUIT:  # Quit
			done = True
		elif ev.type == pygame.KEYDOWN:  # Keypress
			keypress = True
			if ev.key == pygame.K_w:
				changeY = -1
			elif ev.key == pygame.K_s:
				changeY = 1
			if ev.key == pygame.K_d:
				changeX = 1
			elif ev.key == pygame.K_a:
				changeX = -1
			elif ev.key == pygame.K_SPACE:
				player.speeds = [0, 0]

	player.update(changeX, changeY, *BOUNDARIES)

	screen.fill(GREY)
	pygame.draw.rect(screen, BLACK, (player.coords[0]-10, player.coords[1]-10, 20, 20))

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
		# TODO: Draw nicer
		pygame.draw.polygon(screen, bound.colour, bound.pointList)

	# Sort screen
	pygame.display.flip()
	clock.tick(FPS)

pygame.quit()
