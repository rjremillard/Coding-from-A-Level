"""
Evaluates an expression tree
"""


# Get input
tree = [input("Root\n> ")]
while tree[-1] in "+-/*":
	tree.extend([input("Left child\n> "), input("Right child\n> ")])

# Make postfix expression
expr = [tree[0]]
for i in range(1, len(tree)-1):
	expr.append(tree[i])
