"""
Demonstrating Concurrent Programming through threads

task1 : Brute-forcing a md5 hash, plaintext "word"
task2 : Brute-forcing a solution to all factors < 100 of an integer, 360
"""

import threading
import time

from hashlib import md5
from itertools import permutations


def task1(hash_: str):
	LETTERS = "abcdefghijklmnopqrstuvwxyz"
	length = 0
	while True:
		length += 1
		for string in permutations(LETTERS, length):
			joined = "".join(string)
			if md5(joined.encode("UTF-8")).hexdigest() == hash_:
				return


def task2(n: int):
	factors = set()
	for i in range(1, 100):
		if not n % i:
			factors.add(i)


if __name__ == "__main__":
	# Arguments
	hashTmp = md5("word".encode("UTF-8"))
	task1Args = (hashTmp.hexdigest(), )
	task2Args = (360, )
	task3Args = (3, 31, 56)

	# Normally, all procedurally
	startNormal = time.time_ns()

	task1(*task1Args)
	task2(*task2Args)

	endNormal = time.time_ns()

	# Concurrently, using threading
	thread1 = threading.Thread(target=task1, args=task1Args, daemon=True)
	thread2 = threading.Thread(target=task2, args=task2Args, daemon=True)

	startThreaded = time.time_ns()

	thread1.start()
	thread2.start()

	endThreaded = time.time_ns()

	# Output
	print(f"""
	Time to run normally:       {endNormal - startNormal} (ns)
	Time to run with threads:   {endThreaded - startThreaded} (ns)
	
	Difference: {abs((endNormal - startNormal) - (endThreaded - startThreaded))} (ns)
""")
