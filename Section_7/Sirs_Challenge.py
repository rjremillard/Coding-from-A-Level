"""
Finding most efficient n% of a given size of hash table
where
	efficiency is measured in the least amount of collisions but lowest size, and
	'n% of given size' = [SET_SIZE] * (n + 1) for n in range [LOW] ≤ n < [HIGH], step [STEP], and
	hash function is [HASH]

each size will be tested [AVG_NUM] amount of times and an average will be drawn

nb.
Jump amount, size, range, and hash function can also be changed to see their effect on collisions
"""

from random import shuffle
import matplotlib.pyplot as plt
from numpy import arange


# Variables & Function that can change
SET_SIZE, JUMP, LOW, HIGH, STEP, AVG_NUM = 100, 1, 0, 1, .01, 5
HASH = lambda item__, size: (item__ ** 2) % size


# Variables to stay
HISTORY = []  # [(size, collisions), ...]
NUMS = list(range(SET_SIZE))


# Setup HashTable class - cannot reuse "Hash_table.py" as need to measure collisions
class HashTable:
	def __init__(self, size: int):
		self.size = size
		self.table = [None for _ in range(size)]
		self.collisions, self.loops = 0, 0

	def add(self, item_: int):
		index = HASH(item_, self.size)

		# To detect looping
		originalIndex = index

		while True:
			if self.table[index] is None:
				self.table[index] = item_
				break

			else:
				self.collisions += 1
				index = (index + JUMP) % self.size

			if index == originalIndex:
				self.loops += 1
				break


# Main loop
for n in arange(LOW, HIGH, STEP):
	# To get average
	collisionsHistory, loopHistory = 0, 0
	for _ in range(AVG_NUM):
		# Set table
		table = HashTable(int(SET_SIZE * (1 + n)))

		# Add all to table
		shuffle(NUMS)
		for item in NUMS:
			table.add(item)

		# Save to history
		collisionsHistory += table.collisions
		loopHistory += table.loops

	# Add to main history
	HISTORY.append((SET_SIZE * (1 + n), collisionsHistory / AVG_NUM, loopHistory / AVG_NUM))

# Output results
print(HISTORY)


# Matplotlib
fig = plt.figure()
ax = fig.add_axes([0, 0, 1, 1])

sizes = [i[0] for i in HISTORY]
counts = [i[1] for i in HISTORY]

ax.bar(sizes, counts)

plt.show()
