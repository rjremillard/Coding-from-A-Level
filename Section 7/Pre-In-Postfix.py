"""
Two holders:

'Conversions', holding functions to convert between Prefix, Infix, and Postfix, which are:
	- Prefix    -> Infix
	- Prefix    -> Postfix
	- Infix     -> Prefix
	- Infix     -> Postfix
	- Postfix   -> Prefix
	- Postfix   -> Infix

'Evaluate', holding functions to evaluate each of Prefix, Infix, and Postfix, which are:
	- evaluatePrefix
	- evaluateInfix
	- evaluatePostfix

** Notes **
1. All functions take inputs in space separated form, ie. A + ( B * C )
"""


# Stack class, acting as data type, for conversions
# Specifically made for this, so won't have all normal stack methods
# Also dynamic for ease of use
class Stack:
	def __init__(self) -> None:
		self.s = []
		self.size = 0

	def pop(self) -> str:
		self.size -= 1
		return self.s.pop(0)

	def pop2(self) -> list:
		return [self.pop() for _ in range(2)]

	def push(self, *args) -> None:
		self.s.insert(0, "".join(args))
		self.size += 1

	def return_(self) -> str:
		return self.s[0]


class Conversions:
	@staticmethod
	def PrefixToInfix(prefix: str) -> str:
		infix = Stack()
		for i in prefix[::-1].split():
			if i.isnumeric():
				infix.push(i)
			else:
				n0, n1 = infix.pop2()
				infix.push("(", n0, i, n1, ")")

		return infix.return_()

	@staticmethod
	def PrefixToPostfix(prefix: str) -> str:
		postfix = Stack()
		for i in prefix[::-1].split():
			if i.isnumeric():
				postfix.push(i)
			else:
				n0, n1 = postfix.pop2()
				postfix.push(n0, n1, i)

		return postfix.return_()

	@staticmethod
	def InfixToPrefix(infix: str) -> str:
		# TODO: InfixToPrefix
		pass

	@staticmethod
	def InfixToPostfix(infix: str) -> str:
		# TODO: InfixToPostfix
		pass

	@staticmethod
	def PostfixToPrefix(postfix: str) -> str:
		prefix = Stack()
		for i in postfix.split():
			if i.isnumeric():
				prefix.push(i)
			else:
				n0, n1 = prefix.pop2()
				prefix.push(i, n1, n0)

		return prefix.return_()

	@staticmethod
	def PostfixToInfix(postfix: str) -> str:
		infix = Stack()
		for i in postfix.split():
			if i.isnumeric():
				infix.push(i)
			else:
				n0, n1 = infix.pop2()
				infix.push("(", n1, i, n0, ")")

		return infix.return_()


class Evaluates:
	@staticmethod
	def evaluatePrefix(prefix: str) -> str:
		stack = Stack()
		for i in prefix[::-1].split():
			if i.isnumeric():
				stack.push(i)
			else:
				n0, n1 = stack.pop2()
				stack.push(str(eval(n0 + i + n1)))

		return stack.return_()

	@staticmethod
	def evaluateInfix(infix: str) -> str:
		return str(eval(infix))  # Kinda cheaty but it works

	@staticmethod
	def evaluatePostfix(postfix: str) -> str:
		stack = Stack()
		for i in postfix.split():
			if i.isnumeric():
				stack.push(i)
			else:
				n0, n1 = stack.pop2()
				stack.push(str(eval(n1 + i + n0)))

		return stack.return_()


# Testcases
if __name__ == "__main__":
	print("""
	--\nPrefix: + * 2 4 / 6 3\nTranslated Infix: %s\nTranslated Postfix: %s\nEvaluated: %s
	--\nInfix: ( ( 2 * 4 ) + ( 6 / 3 ) )\nTranslated Prefix: %s\nTranslated Postfix: %s\nEvaluated: %s
	--\nPostfix: 2 4 * 6 3 / +\nTranslated Prefix: %s\nTranslated Infix: %s\nEvaluated: %s
	--""" % (Conversions.PrefixToInfix("+ * 2 4 / 6 3"), Conversions.PrefixToPostfix("+ * 2 4 / 6 3"),
							Evaluates.evaluatePrefix("+ * 2 4 / 6 3"),
										"None", "None", Evaluates.evaluateInfix("( ( 2 * 4 ) + ( 6 / 3 ) )"),
										Conversions.PostfixToPrefix("2 4 * 6 3 / +"), Conversions.PostfixToInfix("2 4 * 6 3 / +"),
										Evaluates.evaluatePostfix("2 4 * 6 3 / +")))
