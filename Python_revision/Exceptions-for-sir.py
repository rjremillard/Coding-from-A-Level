"""A tutorial, per say, on Exceptions - for sir"""


# You can make your own exceptions to raise later
class MyException(BaseException):
	# Allow own message to be used
	def __init__(self, msg: str = "Exception"):
		super().__init__(msg)
		self.message = msg

	# __str__ is a magic method that defines the output when printed so,
	# when outputted, it will have a different message
	def __str__(self):
		return "Special exception encountered: %s" % self.message


# Example - for if a number is too large
class NumberTooLarge(BaseException):
	def __init__(self, num: int, boundary: int):
		super().__init__("Number too large")
		self.num, self.bound = num, boundary

	def __str__(self):
		return "%d is too large (greater than %d)" % (self.num, self.bound)


# Testing, runs if not imported (is main script)
if __name__ == "__main__":
	num1, num2 = 12, 10
	try:
		if num1 > num2:
			# Raises error, passing it the needed variables
			raise NumberTooLarge(num1, num2)

	# To print the error instead of it halting the program
	# Comment out to see what it looks like otherwise
	except NumberTooLarge as e:
		print(e)
