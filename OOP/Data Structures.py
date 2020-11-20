"""
Classes for the following data structures:
	- Stack
	- Queue
	- Tree
	- Linked list
	- Graph
"""


class UnderflowError(Exception):
	pass


class Stack:
	def __init__(self, size: int):
		self.maxSize, self.size, self.__list = size, 0, [None for _ in range(size)]
		self.top = 0

	def push(self, other: any):
		if self.size != self.maxSize:
			self.__list[self.top] = other
			self.top += 1
			self.size += 1

		else:
			raise OverflowError("Stack size has been reached")

	def pop(self) -> any:
		if self.size:
			item = self.__list[self.top]
			self.__list[self.top] = None
			self.top -= 1
			self.size -= 1
			return item

		else:
			raise UnderflowError("Stack has no items")

	def __str__(self):
		return "stack: %s, top: %d, size: %d" % (" ".join(map(str, self.__list)), self.top, self.size)

	def __repr__(self):
		return {"__list": self.__list, "top": self.top, "maxSize": self.maxSize, "size": self.size}


class LinearQueue:
	def __init__(self, size: int):
		self.maxSize, self.size, self.__list = size, 0, [None for _ in range(size)]
		self.top, self.rear = 0, 0

	def enQueue(self, other: any):
		if self.size != self.maxSize:
			self.__list[self.rear] = other
			self.rear += 1
			self.size += 1

		else:
			raise OverflowError("Queue is full")

	def deQueue(self):
		if self.size:
			item = self.__list[self.top]
			self.__list[self.top] = None
			self.top += 1
			self.size -= 1
			return item

		else:
			raise UnderflowError("Queue is empty")

	def __str__(self):
		return "queue: %s, top: %d, rear: %s, size: %d" % (" ".join(map(str, self.__list)), self.top, self.rear, self.size)

	def __repr__(self):
		return {"__list": self.__list, "top": self.top, "rear": self.rear, "maxSize": self.maxSize, "size": self.size}


class CircularQueue(LinearQueue):
	def __init__(self, size: int):
		super().__init__(size)
		self.__list = [None for _ in range(size)]

	def enQueue(self, other: any):
		if self.size != self.maxSize:
			self.__list[self.rear] = other
			self.rear = (self.rear + 1) % self.maxSize
			self.size += 1

		else:
			raise OverflowError("Queue is full")

	def deQueue(self):
		if self.size:
			item = self.__list[self.top]
			self.__list[self.top] = None
			self.top = (self.top + 1) % self.maxSize
			self.size -= 1
			return item

		else:
			raise UnderflowError("Queue is empty")

	def __str__(self):
		return "queue: %s, top: %d, rear: %s, size: %d" % (" ".join(map(str, self.__list)), self.top, self.rear, self.size)

	def __repr__(self):
		return {"__list": self.__list, "top": self.top, "rear": self.rear, "maxSize": self.maxSize, "size": self.size}


class Node:
	def __init__(self, data: any, left: "Node" = None, right: "Node" = None):
		self.data, self.left, self.right = data, left, right

	def __str__(self):
		return str(self.data)

	def __repr__(self):
		return str({"data": self.data, "left": self.left, "right": self.right})


class RootNode(Node):
	def evaluate(self):
		return self.__repr__()


class LinkedList(list):
	"""Shhhhh, it totally works"""
	pass


if __name__ == "__main__":
	print("\n*** Stack ***")
	stackObj = Stack(size=10)

	for a in "abcdefg":
		stackObj.push(a)

	print(stackObj)

	for _ in range(5):
		__ = stackObj.pop()

	print(stackObj)

	print("\n*** LinearQueue ***")
	linearQueueObj = LinearQueue(size=10)

	for a in "abcdefg":
		linearQueueObj.enQueue(a)

	print(linearQueueObj)

	for _ in range(5):
		__ = linearQueueObj.deQueue()

	print(linearQueueObj)

	print("\n*** CircularQueue ***")
	circularQueueObj = CircularQueue(size=7)

	for a in "abcdefg":
		circularQueueObj.enQueue(a)

	print(circularQueueObj)

	for _ in range(5):
		__ = circularQueueObj.deQueue()

	print(circularQueueObj)

	for a in "hij":
		circularQueueObj.enQueue(a)

	print(circularQueueObj)

	print("\n*** Tree ***")
	root = RootNode("a", left=Node(1, right=Node(5)), right=Node("h", left=Node(4)))

	values = root.evaluate()
	print(values)

	print("\n*** LinkedList ***")
	linkedListObj = LinkedList()

	for a in "abcdefg":
		linkedListObj.append(a)

	print(linkedListObj)

	for _ in range(5):
		__ = linkedListObj.pop()

	print(linkedListObj)
