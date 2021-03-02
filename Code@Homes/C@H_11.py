"""Binary and linear searches"""

# Imports
import tkinter
import timeit

from tkinter import messagebox
from typing import List


# Constants
FONT10 = ("JetBrains mono", 10)
FONT11 = ("JetBrains mono", 11)
PADS = {"padx": 10, "pady": 10}


# Functions
def linear(lst: List[int], target: int) -> bool:
	"""Linear search for `target` in `lst`"""
	for i in lst:
		if i == target:
			return True
	else:
		return False


def binary(lst: List[int], target: int) -> bool:
	"""Recursive, binary, search for `target` in `lst`"""
	if len(lst) > 1 and lst[0] != target:
		mid = len(lst) // 2
		midVal = lst[mid]
		if midVal == target:
			return True
		else:
			if midVal < target:
				return binary(lst[mid:], target)
			else:
				return binary(lst[:mid], target)
	else:
		return False


def searcher(search_type: int):
	"""Gets data, validates, runs the search, and times it
	:param search_type: 0 = linear, 1 = binary
	"""
	nums = entry0.get()
	target = entry1.get()

	if target.isnumeric():
		if "," in nums:
			nums = nums.split(", ")
		elif " " in nums:
			nums = nums.split()
		else:
			messagebox.showerror("Bad input", "List of numbers is badly formatted")
			return

		if all(map(lambda x: x.isnumeric(), nums)):
			# All should be fine now
			if search_type == 0:
				time = timeit.timeit(lambda: linear(nums, target))
				result = linear(nums, target)
			elif search_type == 1:
				time = timeit.timeit(lambda: binary(nums, target))
				result = binary(nums, target)

			messagebox.showinfo(
				"Search Result",
				f"{target} is{'' if result else 'nt'} in {' '.join(nums)}\nThe search took {round(time, 2)}s"
			)
		else:
			messagebox.showerror("Bad Input", "List of numbers does not fully contain integers")
	else:
		messagebox.showerror("Bad Input", "Target is not an integer")


def help_():
	messagebox.showinfo(
		"Help",
		"""
The list of numbers input can be:
	- Space separated integers, or
	- Comma separated integers,
	
eg., 1 2 3 4 / 1, 2, 3, 4
		"""
	)


# Tkinter
window = tkinter.Tk()
window.title = "Searching..."

title = tkinter.Label(master=window, text="Let's get searching...", font=FONT11)
title.grid(row=0, column=0, columnspan=2, **PADS)

inpLabel0 = tkinter.Label(master=window, text="List of numbers: ", font=FONT10)
inpLabel0.grid(row=1, column=0, **PADS)
entry0 = tkinter.Entry(master=window, font=FONT10)
entry0.grid(row=1, column=1, **PADS)

inpLabel1 = tkinter.Label(master=window, text="Target: ", font=FONT10)
inpLabel1.grid(row=2, column=0, **PADS)
entry1 = tkinter.Entry(master=window, font=FONT10)
entry1.grid(row=2, column=1, **PADS)

linearButton = tkinter.Button(master=window, text="Linear Search", command=lambda: searcher(0), font=FONT10)
linearButton.grid(row=3, column=0, **PADS)
binaryButton = tkinter.Button(master=window, text="Binary Search", command=lambda: searcher(1), font=FONT10)
binaryButton.grid(row=3, column=1, **PADS)

helpButton = tkinter.Button(master=window, text="Help", command=help_, font=FONT10)
helpButton.grid(row=4, column=0, columnspan=2, **PADS)

tkinter.mainloop()
