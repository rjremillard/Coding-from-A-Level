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

# Save prefix
prefix = "".join(tree)


# Make infix expression
infixStack = []

for i in tree[::-1]:
	# If number, push to stack
	if i.isnumeric():
		infixStack.insert(0, i)
	# If operator, sort out
	else:
		n0, n1 = infixStack.pop(0), infixStack.pop(0)
		infixStack.insert(0, "(%s%s%s)" % (n0, i, n1))

# Save infix
infix = "".join(infixStack)


# Make postfix expression
postfixStack = []

for i in tree[::-1]:
	# If number, push to stack
	if i.isnumeric():
		postfixStack.append(i)
	# If operator, sort out
	else:
		n0, n1 = postfixStack.pop(), postfixStack.pop()
		postfixStack.append(n0+n1+i)

# Save postfix
postfix = "".join(postfixStack)

print(prefix, infix, postfix, sep="\n")
