import pygame as py

# Constants
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (211, 211, 211)

SIZE = (600, 400)

FPS = 60


# Functions
def tree(x, y, colour=GREEN):
	py.draw.rect(screen, colour, [x, y, 30, 45])
	for mod in range(0, 61, 30):
		py.draw.polygon(screen, colour, [(x-50, y-mod), (x+80, y-mod), (x+15, y-(100+mod))])


def house(x, y, colours=(RED, BLACK)):
	py.draw.rect(screen, colours[0], [x, y, 70, 50])
	py.draw.polygon(screen, colours[1], [(x-20, y), (x+90, y), (x+35, y-40)])


def snowman(x, y, colour=WHITE):
	for r, mod in zip([50, 30, 20], [0, 45, 70]):
		py.draw.circle(screen, colour, (x, y-mod), r)


# Main Pygame stuff
py.init()
screen = py.display.set_mode(SIZE)
clock = py.time.Clock()

done = False
while not done:
	for ev in py.event.get():
		if ev.type == py.QUIT:
			done = True

	# Sort screen
	screen.fill(GREY)

	for func, coords in zip([tree, house, snowman], [(120, 280), (300, 100), (450, 300)]):
		func(*coords)

	py.display.flip()
	clock.tick(FPS)

py.quit()
