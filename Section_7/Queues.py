class Linear:
	def __init__(self, maxsize: int):
		self.front, self.rear, self.size = 1, -1, 0
		self.maxSize = maxsize
		self.queue = []

	def enQueue(self, item):
		self.queue.append(item)
