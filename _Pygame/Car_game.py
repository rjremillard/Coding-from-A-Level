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
import random
import re
import numpy

from typing import Tuple


# Constants / variables
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (211, 211, 211)

FPS = 60
SIZE = (1000, 500)


# Boundary class
class Boundary:
	def __init__(self, equation: str):
		""":param equation: in form y < or > ax + b {c<x<d}, or x < or > ay  + b {c<y<d}"""
		equation = equation.replace(" ", "")

		reMatch = re.match(r"^([xy])([<>])([+\-.\d]+)([xy])([+\-.\d]+){([+\-.\d]+)<\4<([+\-.\d]+)}$", equation)

		if reMatch:
			self.xy1 = reMatch.group(1)
			self.sign = reMatch.group(2)
			self.a = float(reMatch.group(3))
			self.xy2 = reMatch.group(4)
			self.b = float(reMatch.group(5))
			self.range = numpy.arange(float(reMatch.group(6)), float(reMatch.group(7)))
		else:
			raise Exception("Incorrect Equation")

	def inBound(self, x: int, y: int) -> bool:
		if x in self.range and eval(f"{self.xy1} {self.sign} {(self.a * eval(self.xy2)) + self.b}"):
			return True
		return False


# Car class
class Player:
	def __init__(self, colour: Tuple[int, int, int] = BLACK, max_speed: int = 10):
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
	Boundary("y < 0x + 0 {-10000<x<10000}"),  # Bottom
	Boundary("y > 0x + %d {-10000<x<10000}" % SIZE[1]),  # Top
	Boundary("x < 0y + 0 {-10000<y<10000}"),  # Left
	Boundary("x > 0y + %d {-10000<y<10000}" % SIZE[0])  # Right
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

	# Sort screen
	pygame.display.flip()
	clock.tick(FPS)

pygame.quit()
