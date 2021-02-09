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
import re
import numpy

from typing import Tuple


# Constants / variables
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (211, 211, 211)
RED = (255, 0, 0)

pygame.font.init()
FONT = pygame.sysfont.SysFont("Comfortaa", 20)

FPS = 60
SIZE = (1000, 500)
GAME_SIZE = (SIZE[0]-20, SIZE[1]-20)


# Boundary class
class Boundary:
	def __init__(self, equation: str, colour: Tuple[int, int, int] = RED):
		""":param equation: in form y < or > ax + b {c<x<d}{e<y<f}, or x < or > ay  + b {c<x<d}{e<y<f}"""
		equation = equation.replace(" ", "")

		reMatch = re.match(
			r"^([xy])([<>])([+\-.\d]+)([xy])([+\-.\d]+){([+\-.\d]+)<x<([+\-.\d]+)}{([+\-.\d]+)<y<([+\-.\d]+)}$",
			equation
		)

		if reMatch:
			self.xy1 = reMatch.group(1)
			self.sign = reMatch.group(2)
			self.a = float(reMatch.group(3))
			self.xy2 = reMatch.group(4)
			self.b = float(reMatch.group(5))
			c = float(reMatch.group(6))
			d = float(reMatch.group(7))
			self.xRange = numpy.arange(c, d)
			e = float(reMatch.group(8))
			f = float(reMatch.group(9))
			self.yRange = numpy.arange(e, f)

			# For drawing the line
			if self.xy1 == "y":
				self.start = self.toInt((c, self.a * c + self.b))
				self.end = self.toInt((d, self.a * d + self.b))
			else:
				self.start = self.toInt((self.a * c + self.b, c))
				self.end = self.toInt((self.a * d + self.b, d))

			self.colour = colour
		else:
			raise Exception("Incorrect Equation")

	def inBound(self, x: float, y: float) -> bool:
		"""Calculate if certain coordinates are bound by the inequality"""
		if x in self.xRange and y in self.yRange and eval(f"{self.xy1} {self.sign} {(self.a * eval(self.xy2)) + self.b}"):
			return True
		return False

	@staticmethod
	def toInt(a: Tuple[float, ...]) -> Tuple[int, ...]:
		return tuple(map(int, a))


# Car class
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
	Boundary("y < 0x + 0 {-10000<x<10000}{-1000<y<0}"),  # Bottom
	Boundary("y > 0x + %d {-10000<x<10000}{%d<y<%d}" % (GAME_SIZE[1], GAME_SIZE[1], GAME_SIZE[1]+1000)),  # Top
	Boundary("x < 0y + 0 {-1000<x<0}{-10000<y<10000}"),  # Left
	Boundary("x > 0y + %d {%d<x<%d}{-10000<y<10000}" % (GAME_SIZE[0], GAME_SIZE[0], GAME_SIZE[0]+1000)),  # Right
	Boundary("y < .25x + 0 {-10000<x<10000}{-10000<y<10000}"),
	Boundary("y < 0x + 300 {100<x<300}{100<y<300}")
]
player = Player()

done = False
while not done:
	changeX, changeY = 0, 0
	for ev in pygame.event.get():
		if ev.type == pygame.QUIT:  # Quit
			done = True
		elif ev.type == pygame.KEYDOWN:  # Keypress
			if ev.key == pygame.K_w:
				changeY = -2
			elif ev.key == pygame.K_s:
				changeY = 2
			if ev.key == pygame.K_d:
				changeX = 2
			elif ev.key == pygame.K_a:
				changeX = -2
			elif ev.key == pygame.K_SPACE:
				player.speeds = [0, 0]

	player.update(changeX, changeY, *BOUNDARIES)

	screen.fill(GREY)
	pygame.draw.rect(screen, BLACK, (*player.coords, 20, 20))

	# Draw boundaries
	for bound in BOUNDARIES:
		pygame.draw.line(screen, bound.colour, bound.start, bound.end)

	# Helpful text
	speedXText = FONT.render(f"Speed x: {player.speeds[0]}", 0, BLACK)
	speedYText = FONT.render(f"Speed y: {-1*player.speeds[1]}", 1, BLACK)
	coordsText = FONT.render(f"Coords:  {player.coords[0]}, {player.coords[1]}", 2, BLACK)

	screen.blit(speedXText, (10, 10))
	screen.blit(speedYText, (10, 22))
	screen.blit(coordsText, (10, 34))

	# Sort screen
	pygame.display.flip()
	clock.tick(FPS)

pygame.quit()
