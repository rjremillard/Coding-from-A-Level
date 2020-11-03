"""
Converts between two arbitrary bases
Goes to denary then to wanted base
"""

# Constants
VALUES = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15}
REV_VALUES = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}


# Functions
def valueOf(x: str) -> int:
	return VALUES[x] if x in VALUES else int(x)


def revValueOf(x: int) -> str:
	return REV_VALUES[x] if x in REV_VALUES else str(x)


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
