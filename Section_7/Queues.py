# Classes
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
		return self.queue[-1]

	def isEmpty(self):
		return self.size == 0


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


# Testing

queue = Circular(int(input("Size: ")))  # Change to Circular to test

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
		queue.enQueue(item=input("Item to add: "))

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
