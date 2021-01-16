from typing import List
from time import time_ns, sleep


def firstFit(arr: List[int], max_: int):
	"""
	Iterates through the array of weights and fits them into the first bin that fits
	:param arr: Iterable of integers, weights
	:param max_: Int, maximum weight of the bin
	"""
	sleep(.1)

	bins = [[0, []]]
	for weight in arr:
		for bin_ in bins:
			if bin_[0] + weight <= max_:
				bin_[0] += weight
				bin_[1].append(weight)
			else:
				bins.append([weight, [weight]])
				break

	bins.sort(reverse=True)
	return bins[0]


def bestFit(arr: List[int], max_: int):
	"""
	Iterates through the array of weights and fits them into the bin with the least capacity, that would still fit
	:param arr: Iterable of integers, weights
	:param max_: Int, maximum weight of the bin
	"""
	sleep(.1)

	bins = [[0, []]]
	for weight in arr:
		for bin_ in sorted(bins):
			if bin_[0] + weight <= max_:
				bin_[0] += weight
				bin_[1].append(weight)
			else:
				bins.append([weight, [weight]])
				break

	bins.sort(reverse=True)
	return bins[0]


if __name__ == "__main__":
	maximum = int(input("Max Weight: "))
	weights = list(map(int, input("Space Separated Weights: ").split()))

	# As processing time is very low, have to sleep for .1s, then remove it to see an actual time, hence "- 1e8"

	start = time_ns()
	firstCombo, firstSum = firstFit(weights, maximum)
	end = time_ns()
	firstTime = end - start - 1e8

	start = time_ns()
	bestCombo, bestSum = bestFit(weights, maximum)
	end = time_ns()
	bestTime = end - start - 1e8

	print(f"""
	Maximum Weight:         {maximum}
	List of Weights:        {weights}
	
	First Fit Combination:  {firstCombo}
	First Fit Sum:          {firstSum}
	First Fit Time:         {firstTime}
	
	Best Fit Combination:   {bestCombo}
	Best Fit Sum:           {bestSum}
	Best Fit Time:          {bestTime}
""")
