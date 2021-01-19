"""
Ranks the webpages given a graph of their connections, using the formula:
	PR(A) = (1-d) + d(PR(T1)/C(T1) + ... + PR(Tn)/C(Tn))

Where PR is the pageRank algorithm, d is the damping factor, T1 is the next page, and C is the total number of links
	from that page

The pages will be read from the JSON file `C@H_10.json`, where they should be saved in the following form:
	{
		"Page Name" : {"incoming": [Incoming pages], "outbound": number of outbound links
	}
"""


import json

from collections import defaultdict
from matplotlib import pyplot

# Constants
DAMPING = 0.85

# Variables
pageRanks = defaultdict(lambda: 1.00)
with open("C@H_10.json", "r") as f:
	pageInfo = json.load(f)


# PR function
def PR(page_name: str) -> float:
	"""
	Calculates and returns the new rank of `page name`, uses the formula:
		PR(A) = (1-d) + d(PR(T1)/C(T1) + ... + PR(Tn)/C(Tn))

	Also saves the new rank to the defaultdict of all ranks
	As it uses a defaultdict, in the calculation, if any rank is yet to be set it will be taken as 1
	The calculation does not effect any other pages' ranks

	:param page_name: Name of page to calculate and change the rank of
	:return: The new rank of `page name`
	"""
	sum_, current = 0, None

	# Start summation
	for page in pageTable[page_name]["incoming"]:
		sum_ += pageRanks[page] / pageTable[page]["outbound"]

	rank = (1-DAMPING) + sum_ * DAMPING
	pageRanks[page_name] = rank

	return rank


# Updates all pages' rank
def update(page_list: list) -> list:
	"""
	Iterates through the given list of page names updating each page's rank, also returns a list of all the new ranks
	:param page_list: List of all pages to be updated
	:return: List of the updated ranks
	"""
	for page in page_list:
		rank = PR(page)
		yield rank


# Main code
pageTable = pageInfo["page table"]
pageList = pageInfo["page list"]

while True:
	goAgain = input("Update page ranks? (Y/n)\n> ").lower()

	if goAgain == "y":
		chart = pyplot.bar(range(len(pageList)), list(update(pageList)))
		pyplot.ylabel("Rank")
		pyplot.xticks(range(len(pageList)), pageList)

		pyplot.show()
	else:
		input("Press any key to exit")
		exit()
