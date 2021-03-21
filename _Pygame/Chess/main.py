"""Chess!"""

grid = [
	["Rook B", "Knight B", "Bishop B", "Queen B", "King B", "Bishop B", "Knight B", "Rook B"],
	["Pawn B"] * 8,
	[""] * 8,
	[""] * 8,
	[""] * 8,
	[""] * 8,
	["Pawn W"] * 8,
	["Rook W", "Knight W", "Bishop W", "King W", "Queen W", "Bishop W", "Knight W", "Rook W"]
]


def help_():
	print("""
	*** Type 'help' to see this message ***
	
		- Moves are to be two sets of zero-indexed coordinates:
			1. The start square
			2. The end square
			Ie., 41 43 (King's Pawn opening)
		
	""")

	input("Press enter to continue...")


def prettyPrint(grid_: list, center: int = 8):
	print(" | ".join(str(i).center(center) for i in range(0, 9)))
	# TODO: Fix the printing
	for line, n in zip(grid_, range(1, 9)):
		print('-' * 96)
		print(str(n).center(center), end=" | ")
		print(" | ".join(i.center(center) for i in line))


help_()
game, player = True, 0
while game:
	prettyPrint(grid)
	move = input(f"{'Black' if player else 'White'}'s move\n> ")

	if move.lower() == "help":
		help_()
	else:
		if all(map(lambda x: x.isnumeric(), move.replace(" ", ""))):
			from_, to = move.split()
			from_, to = list(map(int, tuple(from_))), list(map(int, tuple(to)))
			piece = grid[from_[1]-1][from_[0]-1]

			if piece:
				valid = False
				piece, colour = piece.split()

				if piece == "Pawn":
					if

				grid[from_[1] - 1][from_[0] - 1] = ""
				grid[to[1] - 1][to[0] - 1] = piece + " " + colour
				player = (player + 1) % 2
			else:
				print(f"There is no piece at {from_}")

		else:
			print("Invalid input, please consult the help menu")
