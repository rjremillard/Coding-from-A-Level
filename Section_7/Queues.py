"""
:: Classes ::
Made as classes as all data types are in python
"""


class Linear:
	def __init__(self, size: int):
		self.front, self.rear, self.size = 0, -1, 0
		self.maxSize = size
		self.queue = [None for _ in range(size)]

	def enQueue(self, item: any):
		if self.isFull():
			raise IndexError("Queue Full")
		else:
			self.size += 1
			self.rear += 1
			self.queue[self.rear] = item

	def deQueue(self):
		if self.isEmpty():
			raise IndexError("Queue Empty")
		else:
			toReturn = self.queue[self.front]
			self.queue[self.front] = None
			self.size -= 1
			self.front += 1
			return toReturn

	def isFull(self):
		return bool(self.queue[-1])

	def isEmpty(self):
		return not self.size


class Circular(Linear):
	# Inherited: __init__, isEmpty
	def enQueue(self, item: any):
		if self.isFull():
			raise IndexError("Queue Full")
		else:
			self.size += 1
			self.rear = (self.rear + 1) % self.maxSize
			self.queue[self.rear] = item

	def deQueue(self):
		if self.isEmpty():
			raise IndexError("Queue Empty")
		else:
			toReturn = self.queue[self.front]
			self.queue[self.front] = None
			self.front = (self.front + 1) % self.maxSize
			self.size -= 1
			return toReturn

	def isFull(self):
		return self.size == self.maxSize


class Priority:
	def __init__(self, size: int):
		self.front, self.rear, self.size = 0, -1, 0
		self.maxSize = size
		self.queue = [[None, 4] for _ in range(size)]

	def enQueue(self, item: any, priority: int):
		if self.isFull():
			raise IndexError("Queue full")
		else:
			self.size += 1
			self.rear += 1
			self.queue[self.rear] = [item, priority]
			self.queue.sort(key=lambda x: x[1])

	def deQueue(self):
		if self.isEmpty():
			raise IndexError("Queue empty")
		else:
			toReturn = self.queue[self.front]
			self.queue[self.front] = [None, 4]
			self.size -= 1
			self.front += 1
			return toReturn

	def isFull(self):
		return bool(self.queue[-1][0])

	def isEmpty(self):
		return not self.size


# Testing
def main():
	for i in ["l", "c", "p"]:
		if i == "l":
			print(":: Linear ::")
			queue = Linear(int(input("Size: ")))
		elif i == "c":
			print(":: Circular ::")
			queue = Circular(int(input("Size: ")))
		else:
			print(":: Priority ::")
			queue = Priority(int(input("Size: ")))

		while True:
			choice = input("""
			1. Add
			2. Remove
			3. Check Full
			4. Check Empty
			5. Display
			6. Quit
			:: """)

			if choice == "1":
				if i == "p":
					queue.enQueue(input("Item to add: "), int(input("Priority (0-3): ")))
				else:
					queue.enQueue(input("Item to add: "))

			elif choice == "2":
				print("Removed: %s" % queue.deQueue())

			elif choice == "3":
				print("Queue is%s full" % ("" if queue.isFull() else "n't"))

			elif choice == "4":
				print("Queue is%s empty" % ("" if queue.isEmpty() else "n't"))

			elif choice == "5":
				print("Queue is: %s; Front is: %d; Rear is: %d" % (queue.queue, queue.front, queue.rear))

			elif choice == "6":
				break

			else:
				print("Please enter a number between 1 and 6")


if __name__ == '__main__':
	main()
