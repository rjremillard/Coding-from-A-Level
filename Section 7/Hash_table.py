"""
Uses hash function of: (key ^2) MOD length
None represents no data
False represents data which has been deleted and can be overwritten
Has "Jump" size of 3, unless user says otherwise
"""


class HashTable:
	def __init__(self, size: int, jumpsize: int = 3):
		self.size, self.jump = 0, jumpsize

		# Size, the closest prime to the size inputted
		for prime in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,
		101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211,
		223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347,
		349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467,
		479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617,
		619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761,
		769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919,
		929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997, 1009, 1013, 1019, 1021, 1031, 1033, 1039, 1049, 1051]:
			if prime >= size:
				self.table = [None for _ in range(prime)]
				self.maxSize = prime
				break

	def add(self, item: any):
		if self.isFull():
			raise IndexError("Hash Table is full")

		else:
			index = self.hash(sum(map(ord, item)))

			done = False
			while not done:
				if self.table[index] is None or self.table[index] is False:
					self.table[index] = item
					done = True
					self.size += 1

				else:
					index = (index + self.jump) % self.maxSize

	def remove(self, item: any):
		if self.isEmpty():
			raise IndexError("Hash Table is empty")

		else:
			index = self.hash(sum(map(ord, item)))

			done = False
			while not done:
				if self.table[index] == item:
					done = True
					self.table[index] = False
					self.size -= 1

				elif self.table[index] is None:
					raise IndexError("Item not in table")

				else:
					index = (index + self.jump) % self.maxSize

	def find(self, item: any):
		if self.isEmpty():
			raise IndexError("Hash Table is empty")

		else:
			index = self.hash(sum(map(ord, item)))

			done = False
			while not done:
				if self.table[index] == item:
					return True

				elif self.table[index] is None:
					return False

				else:
					index = (index + self.jump) % self.maxSize

	def hash(self, item: int) -> int:
		return (item ** 2) % self.maxSize

	def isFull(self) -> bool:
		return self.size == self.maxSize

	def isEmpty(self) -> bool:
		return self.size == 0


# Testing
def main():
	stop = False
	table = HashTable(int(input("Size (to be rounded to closest prime): ")))
	while not stop:
		choice = input("""
		1. Add
		2. Remove
		3. Print
		4. Find
		5. Quit
		> """)

		if choice == "1":
			table.add(input("Item to add: "))

		elif choice == "2":
			table.remove(input("Item to remove: "))

		elif choice == "3":
			print("Table: %s" % ", ".join(map(str, table.table)))

		elif choice == "4":
			print("Item is%s in table" % ("" if table.find(input("Item to find: ")) else "n't"))

		elif choice == "5":
			stop = True

		else:
			print("Enter a number between 1-4")


# So can inherit
if __name__ == '__main__':
	main()
