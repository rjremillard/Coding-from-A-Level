import math


def me(num: int) -> list:
	numbers = [True for _ in range(num + 1)]
	for i in range(2, math.floor(math.sqrt(num)) + 1):
		if numbers[i]:
			j = i ** 2
			while j < num:
				numbers[j] = False
				j += i
	return numbers[2:-1]


def alex(n):
	numbers = [True for i in range(n + 1)]
	for i in range(2, math.ceil(math.sqrt(n)) + 1):
		if numbers[i]:
			j = i ** 2
			while j <= n:
				numbers[j] = False
				j += i
	return numbers[2:]


def oliver(end):
	marks = [True] * end
	for i in range(2, round(end ** 0.5)):
		if marks[i] == True:
			for x in range(i ** 2, end, i):
				marks[x] = False
	return marks


if __name__ == '__main__':
	import timeit
	import threading

	import matplotlib.pyplot as plt

	ns = []
	for i in range(0, 1000, 20):
		ns.append(i)

	# Not using Patrick, Isobel, or Rowan as were all very slow
	# Normalised others to return same data

	TIMES = {}

	def timer(func: callable, name: str):
		times = []
		for num in ns:
			time = timeit.timeit(lambda: func(num), number=10000)
			times.append(time)
			print(f"person={name}, num={num}, time={time}")
		TIMES[name] = times


	threads = []
	for person in [(me, "me"), (alex, "alex"), (oliver, "oliver")]:
		thread = threading.Thread(target=timer, args=(person[0], person[1]))
		thread.start()
		threads.append(thread)

	for thread in threads:
		thread.join()

	for person in TIMES:
		plt.plot(ns, TIMES[person], label=person)

	plt.legend()
	plt.show()
