"""Converts between ascii and binary"""


def toBinary(string: str) -> str:
	return " ".join(bin(ord(i))[2:] for i in string)


def toAscii(string: str) -> str:
	return "".join(chr(int(i, 2)) for i in string.split())


if input("To Bin or ASCII? (b/a)\n> ") == "b":
	print(toBinary(input("> ")))

else:
	with open("Ascii.txt", "w") as f:
		f.write("\n".join(toBinary(input("> ")) for _ in range(int(input("Lines?\n> ")))))

