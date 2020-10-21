"""
Evaluates an expression tree
"""


# Get input
tree = [input("Root\n> ")]
while len([i for i in tree if i in "+-/*"]) != len([i for i in tree if i.isnumeric()]) - 1:
	node = input("%s child\n> " % ("Left" if tree[-1] in "+-/*" else "Right"))
	tree.append(node)

print(tree)

# Make postfix expression
expr = []
for i in range(1, len(tree)-1):
	if tree[i].isnumeric() and tree[i+1].isnumeric():
		expr.extend([tree[i], tree[i+1], tree[i-1]])
		# TODO: Fix

expr.append(tree[0])
print(expr)
