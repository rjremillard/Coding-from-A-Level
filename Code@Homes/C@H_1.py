"""
Hierarchical chart:
		:: Inputs    : Digits
Program :: Processes : Loop through every possible number in range
		:: Outputs   : All possible pins
"""

digits = int(input("Digits: "))

for i in range(int(.999999999 * (10 ** digits)) + 1):
	print(("0" * (digits - len(str(i))) if len(str(i)) < digits else "") + str(i))

# Re-upload - alternative interpretation of instructions

import itertools

"""
Hierarchical chart:
		:: Inputs    : Digits
Program :: Processes : Loop through every possible combo of inputs
		:: Outputs   : All possible pins
"""

digits = input("Digits known (space separated): ").split()

print("\n".join(["".join(i) for i in itertools.permutations(digits)]))

