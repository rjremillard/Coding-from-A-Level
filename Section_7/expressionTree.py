"""
Nicely: inputs, evaluates, and outputs an expression tree in postfix / reverse Polish notation
Currently only works with depth 2
"""


# Get root
tree = [input("Root\n> ")]
# If <amount of operators> = <amount of numbers> - 1, tree is complete
# Input ends up being prefix
while len([i for i in tree if i in "+-/*"]) != len([i for i in tree if i.isnumeric()]) - 1:
	# If node before was operator, next should be left child, otherwise, right
	node = input("%s child\n> " % ("Left" if tree[-1] in "+-/*" else "Right"))
	tree.append(node)

print(tree)


# Make postfix expression
expr = []

# If "even" tree (both sides end in 2 numbers)
if not len([i for i in tree if i.isnumeric()]) % 2:
	for i in range(len(tree)):
		if tree[i] in "+-*/" and tree[i+1].isnumeric():
			expr.extend([tree[i+1], tree[i+2], tree[i]])

	# Add root at end
	expr.append(tree[0])
	print(expr)

# TODO: Uneven tree
