"""
Nicely: inputs, evaluates, and outputs an expression tree in postfix / reverse Polish notation
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
# Skip root
for i in range(1, len(tree)):
	if tree[i].isnumeric() or tree[i-1].isnumeric():
		expr.append(tree[i])
		# TODO: Fix

# Add root at end
expr.append(tree[0])
print(expr)
