def linear(n):
	a = 0
	for i in range(n):
		a += i


def squared(n):
	a = 0
	for i in range(n):
		for j in range(n):
			a += j


def cubed(n):
	a = 0
	for i in range(n):
		for j in range(n):
			for l in range(n):
				a += l


if __name__ == "__main__":
	import time
	import threading
	import asyncio
	import matplotlib.pyplot as plt
	
	from collections import defaultdict

	funcs = [("linear", linear), ("squared", squared), ("cubed", cubed)]
	allTimes = defaultdict(list)

	nMax = 1001
	ns = list(range(0, nMax, 50))

	def timer(func, name):
		times = []
		for n in ns:
			print(f"Log: name={name},\tn={n} ({round(100*n/nMax, 2)})%")
			start = time.time()
			func(n)
			time.sleep(.001)
			end = time.time()

			times.append(end - start)

		allTimes[name] = times

	threads = []
	for f in funcs:
		thread = threading.Thread(target=timer, args=(f[1], f[0]))
		thread.start()
		threads.append(thread)

	for t in threads:
		t.join()

	for f in funcs:
		plt.plot(ns, allTimes[f[0]], label=f[0])

	plt.legend()
	plt.show()
