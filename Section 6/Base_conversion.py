"""
Converts between two arbitrary bases
Goes to denary then to wanted base
"""


# Functions
def valueOf(x: str) -> int:
	return ord(x) - 55 if x.isalpha() else int(x)


def revValueOf(x: int) -> str:
	return chr(x + 55) if x > 9 else str(x)


# Inputs
oldBase, string, newBase = int(input("Current base: ")), input("String of current number: ")[::-1], \
	int(input("Desired base: "))

# Get denary
denary = sum(valueOf(string[i]) * (oldBase ** i) for i in range(len(string)))

# Get max power
power = 1
while newBase ** power < denary:
	power += 1

power -= 1

# Get new number
newString = ""
for i in range(power, -1, -1):
	newString += revValueOf(denary // newBase ** i)
	denary %= newBase ** i

# Output
print("%s, converted from %d to base %d, is %s" % (string, oldBase, newBase, newString))
