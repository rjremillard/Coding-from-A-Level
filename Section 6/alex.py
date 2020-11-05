with open("teehee.txt", "r") as f:
	print("".join(map(chr, map(lambda x: int(x, 2), f.read().split()))))
