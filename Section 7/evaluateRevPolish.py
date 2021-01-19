"""
Evaluating Reverse Polish Notation
"""

from math import ceil

expr = input("Expression, space separated: ").split()
stack = []

for n in expr:
	if n.isnumeric():
		stack.append(n)
	else:
		stack.append(eval("%s%s%s" % (stack.pop(), n, stack.pop())))

print(stack[0])
