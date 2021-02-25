"""Recursive binary tree stuff"""

import random


class Leaf:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

	def __add__(self, other):
		if other.data < self.data:
			if self.left:
				self.left + other
			else:
				self.left = other
		else:
			if self.right:
				self.right + other
			else:
				self.right = other

	def summer(self, sum_=0):
		if self.left:
			sum_ += self.left.summer()
		if self.right:
			sum_ += self.right.summer()

		return sum_ + self.data


# Setup tree
head = Leaf(10)

# Make list of numbers to add to tree, and shuffle
nums = list(range(random.randint(2, 100)))
random.shuffle(nums)

# Add numbers to tree
for i in nums:
	head + Leaf(i)

print(f"Numbers: {nums}\n\nActual sum: {sum(nums)}\nRecursive sum: {head.summer()-10}")
