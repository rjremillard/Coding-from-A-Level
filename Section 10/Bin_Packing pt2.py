"""
Calculates, and graphs, the efficiency of the following bin packing algorithms:
	- First Fit
	- Best Fit
	- Modified First Fit Decreasing

Sometimes, the program will throw an index error so please just rerun
"""

import random
import threading
import Bin_Packing as Bp
import numpy as np

from typing import List, Callable
from time import time_ns, sleep
from matplotlib import pyplot


def modifiedFirstFitDecreasing(arr: List[int], max_: int):
	"""
	Following steps from https://en.wikipedia.org/wiki/Bin_packing_problem
	:param arr: List of integers, weights
	:param max_: Int, maximum weight of the bin
	"""

	bins = []
	weights = arr

	# Sort by class
	large, medium, small, tiny = [], [], [], []
	for weight in weights:
		if weight > 1/2 * max_:
			large.append(weight)
		elif weight > 1/3 * max_:
			medium.append(weight)
		elif weight > 1/6 * max_:
			small.append(weight)
		else:
			tiny.append(weight)

	for class_ in large, medium, small, tiny:
		if class_:
			class_.sort()

	# Step 1: Make bin for every large weight
	for weight in large[::-1]:
		bins.append([weight, [weight]])
	# Bins are now largest to smallest

	# Step 2: Add in mediums
	bins.sort(reverse=True)
	for bin_ in bins:
		if bin_[0] + medium[0] <= max_:
			bin_[0] += medium[-1]
			bin_[1].append(medium[-1])
			del medium[0]

	# Step 3: Add smalls
	for bin_ in bins[::-1]:
		# If doesn't have a medium in
		if len(bin_[1]) == 1:
			if bin_[0] + small[0] + (small[1] if len(small) > 1 else 0) <= max_:
				bin_[0] += small[0]
				bin_[1].append(small[0])
				del small[0]

				for weight in small[::-1]:
					if bin_[0] + weight <= max_:
						bin_[0] += weight
						bin_[1].append(weight)
						del small[small.index(weight)]

	# Step 4: Add the rest that fit
	allWeights = []
	for lst in [medium, small, tiny]:
		allWeights.extend(lst)

	allWeights.sort()
	binIndex = 0
	while binIndex < len(bins):
		bin_ = bins[binIndex]
		if bin_[0] + allWeights[0] > max_:
			binIndex += 1
		else:
			for weight in allWeights[::-1]:
				if bin_[0] + weight <= max_:
					bin_[0] += weight
					bin_[1].append(weight)
					del allWeights[allWeights.index(weight)]

	# Step 5: Sort out the remaining weights, using FFD
	FFDBins = [[0, []]]
	for weight in sorted(allWeights, reverse=True):
		for bin_ in FFDBins:
			if bin_[0] + weight <= max_:
				bin_[0] += weight
				bin_[1].append(weight)
				break
		else:
			FFDBins.append([weight, [weight]])

	bins.extend(FFDBins)
	bins.sort()

	return bins


def efficiency(arr: List[int], bins: List[List[int]], max_: int):
	"""
	Calculates efficiency of the packing, using sir's calculation: ∑(weights) / (number of bins * max weight)
	:param arr: List of integers, weights
	:param bins: List of all bins made by the packing algorithm
	:param max_: Int, maximum weight of the bin
	"""

	return sum(arr) / (len(bins) * max_)


def timer(func: Callable, args: tuple = None):
	start = time_ns()
	sleep(.1)
	return_ = func(*args)
	return return_, time_ns() - start - 1e8


if __name__ == "__main__":
	# Runtime variables
	MAX_WEIGHT = 20
	MAX_WEIGHT_INDIV = 15
	allResults = []

	# Get all bins
	for maxLen in range(20, 101, 5):
		weights = [random.randint(1, MAX_WEIGHT_INDIV) for _ in range(maxLen)]

		firstBins, firstTime = timer(Bp.firstFit, (weights, MAX_WEIGHT))
		bestBins, bestTime = timer(Bp.bestFit, (weights, MAX_WEIGHT))
		MFFDBins, MFFDTime = timer(modifiedFirstFitDecreasing, (weights, MAX_WEIGHT))

		firstEff = efficiency(weights, firstBins, MAX_WEIGHT)
		bestEff = efficiency(weights, bestBins, MAX_WEIGHT)
		MFFDEff = efficiency(weights, MFFDBins, MAX_WEIGHT)

		allResults.append((firstEff, bestEff, MFFDEff))

		print(f"\rWorking..., max length of: {maxLen}", end="")

	# Plot
	X = range(20, 101, 5)

	for index, colour in zip(range(3), ["red", "green", "blue"]):
		Y = [result[index] for result in allResults]
		pyplot.scatter(X, Y, color=colour)
		# https://stackoverflow.com/questions/22239691/code-for-best-fit-straight-line-of-a-scatter-plot-in-python
		pyplot.plot(np.unique(X), np.poly1d(np.polyfit(X, Y, 1))(np.unique(X)), color=colour)

	pyplot.xlabel("Number of Weights")
	pyplot.ylabel("Efficiency")

	pyplot.legend(labels=("First Fit", "Best Fit", "Modified First Fit Decreasing"))

	pyplot.show()
