class Stack:
	def __init__(self, maxsize: int):
		self.stack = [None for _ in range(maxsize)]
		self.top, self.size, self.maxSize = -1, 0, maxsize

	def push(self, item: any):
		if self.isFull():
			raise IndexError("Stack Full")
		else:
			self.top += 1
			self.size += 1
			self.stack[self.top] = item

	def pop(self):
		if self.isEmpty():
			raise IndexError("Stack Empty")
		else:
			toReturn = self.stack[self.top]
			self.stack[self.top] = None
			return toReturn

	def isFull(self):
		return self.size == self.maxSize

	def isEmpty(self):
		return not self.isFull()
