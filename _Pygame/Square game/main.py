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
import json
import time

from game_objects import *
from game_constants import *


# Handy function
def isHit(player_x: int, player_y: int, other_x: int, other_y: int) -> bool:
	return player_x - 2 < other_x < player_x + 22 and player_y - 2 < other_y < player_y + 22


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

# Player, enemies, and collectables
player = Player(3)
enemies = [Enemy(1, RED), Enemy(1.2, RED), Enemy(1.3, RED)]
touches = [0 for _ in range(len(enemies))]
collectables = [Collectable("speed", 6, (650, 200)), Collectable("health", 10, (100, 600))]

# Game variables
done, keypress, dead, scoreSaved = False, False, False, False
keysDown = {pygame.K_w: False, pygame.K_s: False, pygame.K_a: False, pygame.K_d: False}
aliveTime, effects = 0, 0
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
					keypress = True
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

		# Update player
		player.update(*directions, *BOUNDARIES)
		pygame.draw.rect(screen, player.colour, (player.coords[0]-10, player.coords[1]-10, 20, 20))

		# Update enemies
		for enemy in enemies:
			# If we move, enemies move
			if any(player.speeds):
				enemy.update(player.coords, *BOUNDARIES)
			pygame.draw.rect(screen, enemy.colour, (enemy.coords[0]-10, enemy.coords[1]-10, 20, 20))

			# Check if player has been hit
			if isHit(*player.coords, *enemy.coords):
				touches[enemy.number] += 1
			else:
				touches[enemy.number] = 0

		# Update collectables
		for coll in collectables:
			if coll.alive:
				pygame.draw.rect(screen, coll.colour, (coll.coords[0]-5, coll.coords[1]-5, 10, 10))
				if isHit(*player.coords, *coll.coords):
					coll.alive = False
					player.effect = [coll.type, coll.duration]
					effects += 1

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
		deathText = FONT.render(
			f"Death timer: {round(max(touches)/FPS, 2)}s of {2 if player.effect[0] == 'health' else 1}s", 3, BLACK)
		screen.blit(deathText, (10, 46))

		# Alive timer
		aliveText = FONT.render(f"Alive timer: {round(aliveTime/FPS, 2)}s", 4, BLACK)
		screen.blit(aliveText, (10, 58))

		# Effects
		effectText0 = FONT.render(f"Effect: {player.effect[0]}", 5, BLACK)
		effectText1 = FONT.render(f"Time left: {player.effect[1]}", 6, BLACK)

		screen.blit(effectText0, (10, 78))
		screen.blit(effectText1, (10, 90))

	# Draw boundaries
	for bound in BOUNDARIES:
		pygame.draw.polygon(screen, bound.colour, bound.pointList)

	# Deal with death
	if max(touches) >= (FPS * (2 if player.effect[0] == "health" else 1)):
		if not scoreSaved:
			# Take name input from user
			name = ""

			# Save score with username
			with open("scores.json", "r") as f:
				pastScores = json.load(f)

			pastScores.append([list(time.gmtime()), aliveTime / (len(collectables) - effects + 1)])
			with open("scores.json", "w") as f:
				json.dump(pastScores, f)

			scoreSaved = True

		# Other dead stuff
		dead = True
		death0 = BIG_FONT.render("You have died", -10, BLACK)
		death1 = FONT.render(f"Score: {aliveTime / (len(collectables) - effects + 1)}", -11, BLACK)
		death2 = FONT.render(f"Highscore: {max(pastScores, key=lambda x: x[1])[1]}", -12, BLACK)

		screen.blit(death0, (SIZE[0]/2 - 60, SIZE[1]/2 - 20))
		screen.blit(death1, (SIZE[0]/2 - 55, SIZE[1]/2 + 10))
		screen.blit(death2, (SIZE[0]/2 - 55, SIZE[1]/2 + 22))

	# Sort screen
	pygame.display.flip()
	clock.tick(FPS)

pygame.quit()
