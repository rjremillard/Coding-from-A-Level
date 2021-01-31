import tkinter

from matplotlib import pyplot
from typing import Dict
from tkinter import messagebox
from collections import defaultdict


# Constants
FONT10 = ("Comfortaa", 10)
FONT11 = ("Comfortaa", 11)
FONT14 = ("Comfortaa", 14)

PADS = {"padx": 10, "pady": 10}


# Functions
def updateResults(text: str):
	"""Writes the `text` provided to the `resultsText` text box"""
	resultsText.delete("0.0", tkinter.END)
	resultsText.insert(tkinter.END, text)


def plot(results: Dict[str, int], type_: str):
	"""Plots the `results` provided to a pie chart, through matplotlib"""
	labels = results.keys()
	sizes = results.values()

	fig1, ax1 = pyplot.subplots()
	ax1.pie(sizes, labels=labels, autopct="%d")
	ax1.axis('equal')

	pyplot.title(type_ + "\n (%Representatives)")

	pyplot.show()


def roundUp(n: float) -> int:
	"""Returns `n` rounded up to the closest integer"""
	return int(str(n).split(".")[0]) + 1


def roundDown(n: float) -> int:
	"""Returns `n` rounded down to the closest integer"""
	return roundUp(n) - 1


def fractionalPart(n: float) -> float:
	"""Returns the fractional part of `n`"""
	return float("0." + str(n).split(".")[1])


def getData():
	"""Returns data from the inputs, handling ill-formatted data, in a nice format"""
	reprSize = reprEntry.get()
	popSize = popEntry.get()
	statesRaw = statesText.get("0.0", tkinter.END)

	if reprSize.isnumeric() and popSize.isnumeric() and statesRaw:  # If all have data in
		states = {}
		for state in statesRaw.split("\n")[:-1]:
			stateTmp = state.split()
			try:
				states[stateTmp[0]] = int(stateTmp[1])
			except ValueError:  # If not an integer
				messagebox.showerror(title="Input Error", message="Please check your inputs")
				break

		else:  # If loop completes
			return int(reprSize), int(popSize), states

	else:
		messagebox.showerror(title="Input Error", message="Please check your inputs")


def webster():
	"""https://en.wikipedia.org/wiki/Webster/Sainte-Lagu%C3%AB_method"""
	reprSize, popSize, states = getData()
	reprs = defaultdict(lambda: 0)

	while sum(reprs.values()) < reprSize:
		quotients = list(map(lambda x: [states[x] / (2*reprs[x] + 1), x], states.keys()))
		winner = max(quotients)

		reprs[winner[1]] += 1

	updateResults("\n".join(f"{x}: {reprs[x]}" for x in states.keys()))
	plot(reprs, "Webster's Method")


def jefferson():
	"""https://en.wikipedia.org/wiki/D%27Hondt_method"""
	reprSize, popSize, states = getData()
	reprs = defaultdict(lambda: 0)

	while sum(reprs.values()) < reprSize:
		quotients = list(map(lambda x: [states[x] / (reprs[x] + 1), x], states.keys()))
		winner = max(quotients)

		reprs[winner[1]] += 1

	updateResults("\n".join(f"{x}: {reprs[x]}" for x in states.keys()))
	plot(reprs, "Jefferson's Method")


def hamilton():
	"""https://en.wikipedia.org/wiki/Largest_remainder_method"""
	reprSize, popSize, states = getData()
	quota = popSize / reprSize
	reprs = defaultdict(lambda: 0)

	quotients = map(lambda x: [x, states[x] / quota], states.keys())

	for state in quotients:
		reprs[state[0]] = roundDown(state[1])

	fParts = sorted(map(lambda x: [fractionalPart(states[x] / quota), x], states.keys()), reverse=True)

	while sum(reprs.values()) < reprSize:
		reprs[fParts[0][1]] += 1
		del fParts[0]

	updateResults("\n".join(f"{x}: {reprs[x]}" for x in states.keys()))
	plot(reprs, "Hamilton's Method")


# Tkinter window
window = tkinter.Tk()
window.title("Apportionment Algorithms")

title = tkinter.Label(master=window, text=".: Apportionment Algorithms :.", font=FONT14)
title.grid(column=0, row=0, columnspan=3, **PADS)

# Inputs
reprLabel = tkinter.Label(master=window, text="Representative Body Size:", font=FONT11)
reprLabel.grid(column=0, row=1, **PADS)
reprEntry = tkinter.Entry(master=window, font=FONT10)
reprEntry.grid(column=0, row=2, **PADS)

popLabel = tkinter.Label(master=window, text="Population Size:", font=FONT11)
popLabel.grid(column=0, row=3, **PADS)
popEntry = tkinter.Entry(master=window, font=FONT10)
popEntry.grid(column=0, row=4, **PADS)

statesLabel = tkinter.Label(master=window, text="State Names and Sizes (each on own line)\nie. NY 658413:", font=FONT11)
statesLabel.grid(column=0, row=5, **PADS)
statesText = tkinter.Text(master=window, height=6, width=40, font=FONT10)
statesText.grid(column=0, row=6, **PADS)

# Buttons
button1 = tkinter.Button(master=window, command=webster, text="Webster’s Method", font=FONT11)
button1.grid(column=1, row=2, **PADS)

button2 = tkinter.Button(master=window, command=jefferson, text="Jefferson's Method", font=FONT11)
button2.grid(column=1, row=3, **PADS)

button3 = tkinter.Button(master=window, command=hamilton, text="Hamilton's Method", font=FONT11)
button3.grid(column=1, row=4, **PADS)

button4 = tkinter.Button(master=window, command=lambda: updateResults(""), text="Clear Results", font=FONT11)
button4.grid(column=1, row=6, **PADS)

# Results
resultsLabel = tkinter.Label(master=window, text="Results:", font=FONT11)
resultsLabel.grid(column=2, row=1, **PADS)

resultsText = tkinter.Text(master=window, width=40, font=FONT10)
resultsText.grid(column=2, row=2, rowspan=5, **PADS)

tkinter.mainloop()
