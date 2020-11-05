"""
Converts between two arbitrary bases
Goes to denary then to wanted base
"""


# Function
def valueOf(x: int) -> str:
	return chr(x + 55) if x > 9 else str(x)


# Inputs
oldBase, string, newBase = int(input("Current base\n> ")), input("String of current number\n> "), \
	int(input("Desired base\n> "))

# Get denary
denary = int(string, oldBase)

# Get new number
newString = ""
while denary:
	newString += valueOf(denary % newBase)
	denary //= newBase

# Output
print("%s, converted from base %d to base %d, is %s" % (string, oldBase, newBase, newString[::-1]))
