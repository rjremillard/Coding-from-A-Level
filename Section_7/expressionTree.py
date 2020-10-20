"""
Evaluates an expression tree
"""


# Get input
tree = [input("Root\n> ")]
while tree[-1] in "+-/*":
	tree.append(input("Left child\n> "))
	tree.append(input("Right child\n> "))

print(tree)
