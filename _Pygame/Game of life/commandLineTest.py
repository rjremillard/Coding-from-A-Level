import time


def printGrid(grid_):
	print("-----------")
	for line in grid_[:-2]:
		line = map(lambda x: {True: "O", False: "X"}[x], line[:-2])
		print("".join(line))
	print("-----------")


grid = []
for _ in range(7):
	grid.append([False for _ in range(12)])

# Access through [y][x]
grid[2][3] = True
grid[3][3] = True
grid[4][3] = True

while True:
	printGrid(grid)

	for row in range(1, 6):
		for column in range(1, 11):
			neighbours = sum([
				grid[row - 1][column - 1], grid[row - 1][column], grid[row - 1][column + 1],
				grid[row][column - 1], grid[row][column + 1],
				grid[row + 1][column - 1], grid[row + 1][column], grid[row + 1][column + 1]
			])

			if grid[row][column]:
				if neighbours < 2 or neighbours > 3:
					grid[row][column] = False
			else:
				if neighbours == 3:
					grid[row][column] = True

	time.sleep(1)
