"""Classes for game objects used in frontend.py"""

import random

from typing import Tuple, List
from game_constants import *


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
		return self.xRange[0] < x < self.xRange[1] and self.yRange[0] < y < self.yRange[1]


# Player class
class Player:
	def __init__(self, max_speed: float, colour: Tuple[int, int, int] = BLACK):
		self.speeds = [0, 0]
		self.coords = [20, 20]
		self.maxSpeed = max_speed
		self.colour = colour
		self.effect = [None, None]

	def update(self, change_x: int, change_y: int, *boundaries):
		# Check if effected
		if self.effect[0] == "speed":
			mult = 1.01
		else:
			mult = 1

		# Sort speeds to be under max, keep to 2 dp
		self.speeds[0] = round((self.speeds[0] + change_x) * mult, 2)
		if self.speeds[0] > self.maxSpeed:
			self.speeds[0] = self.maxSpeed

		self.speeds[1] = round((self.speeds[1] + change_y) * mult, 2)
		if self.speeds[1] > self.maxSpeed:
			self.speeds[1] = self.maxSpeed

		# Apply speeds to coords
		tmpX = self.coords[0] + self.speeds[0]
		tmpY = self.coords[1] + self.speeds[1]

		# Check for collisions
		for boundary in boundaries:
			if boundary.inBound(tmpX, tmpY):
				self.speeds = [0, 0]
				break
		else:
			# No collisions
			self.coords = [round(tmpX, 2), round(tmpY, 2)]

		# Sort effects
		if self.effect != [None, None]:
			if self.effect[1] <= 0:
				self.effect = [None, None]
			else:
				self.effect[1] -= 1


class Enemy:
	enemyNum = 0

	def __init__(self, max_speed: float, colour: Tuple[int, int, int] = RED):
		self.maxSpeed = max_speed
		self.colour = colour
		self.coords = [SIZE[0]-10, SIZE[1]-10]
		self.number = Enemy.enemyNum
		Enemy.enemyNum += 1

	def update(self, player_coords: List[int], *boundaries):
		"""Will move enemy toward player, using a unit vector for the direction. Adds in some random variation too"""
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

		# TODO: Avoid boundaries
		# Apply directions
		tmpX = self.coords[0] + changeX
		tmpY = self.coords[1] + changeY

		# Check for collisions
		for boundary in boundaries:
			if boundary.inBound(tmpX, tmpY):
				# Collision
				break
			# No collisions
			else:
				self.coords = [round(tmpX, 2), round(tmpY, 2)]


class Collectable:
	def __init__(self, type_: str, duration: float, coords: Tuple[int, int], colour: Tuple[int, ...] = GREEN):
		"""
		:param type_: can be one of speed or health
		:param duration: is to be given in seconds
		"""
		self.coords = coords
		self.type = type_
		self.duration = duration * FPS
		self.colour = colour
		self.alive = True
