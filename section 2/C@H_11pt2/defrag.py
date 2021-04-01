"""Goes over the drive,
gathers info,
and bubble sorts the files (most efficient sort for this purpose)

Gives the user the option to delete corrupt files
"""

import re
import tkinter
import time

from tkinter import messagebox
from collections import defaultdict


# Constants
PADS = {"padx": 10, "pady": 10}
drive = []
driveInfo = {}

# Tkinter
window = tkinter.Tk()
window.title("Defraging...")

title = tkinter.Label(master=window, text="Defragger and Info")
title.grid(column=0, row=0, columnspan=3, **PADS)

fileInputLabel = tkinter.Label(master=window, text="File Name Input")
fileInputLabel.grid(column=0, row=1, **PADS)

fileInputEntry = tkinter.Entry(master=window)
fileInputEntry.grid(column=0, row=2, **PADS)

textInputLabel = tkinter.Label(master=window, text="Text Input")
textInputLabel.grid(column=0, row=3, **PADS)

textInputEntry = tkinter.Text(master=window, width=12)
textInputEntry.grid(column=0, row=4, **PADS)


def getAndClean():
	global drive
	fileName = fileInputEntry.get()
	textInput = textInputEntry.get("1.0", tkinter.END)

	if not len(fileName) and not len(textInput):
		messagebox.showerror("Bad Input", "Please only use one input")
	elif len(fileName):
		with open(fileName, "r") as f:
			drive = [line_.split() for line_ in f.read().split("\n")]
	elif len(textInput):
		drive = [line_.split() for line_ in textInput.split("\n")[:-1]]
	else:
		messagebox.showerror("Bad Input", "Please input something")


inputButton = tkinter.Button(master=window, text="Submit", command=getAndClean)
inputButton.grid(column=0, row=5, **PADS)


def defrag():
	# Get drive info
	global driveInfo, drive
	driveInfo = {
		"files": set(),
		"lengths": defaultdict(lambda: 0),
		"fileMap": []
	}

	for index, line in enumerate(drive):
		file, *fData = line

		if file:
			# Flag corrupt files
			if not bool(re.match(r"[A-Z] [01]{8}$", " ".join(line))):
				drive[index].append("Corrupt")

				driveInfo["files"].add("X")
				driveInfo["lengths"]["X"] += 1
			else:
				driveInfo["files"].add(file)
				driveInfo["lengths"][file] += 1
		else:
			driveInfo["files"].add("Empty")
			driveInfo["lengths"]["Empty"] += 1

	# Sort
	swapped, n = True, 1
	while swapped:
		swapped = False
		for i in range(len(drive) - n):
			if drive[i] > drive[i+1]:
				drive[i], drive[i+1] = drive[i+1], drive[i]
				swapped = True

	# Map new drive
	for line in drive:
		driveInfo["fileMap"].append(line[0] if len(line) == 2 else "X")

	with open("defragOut.txt", "w") as f:
		f.write("\n".join(" : ".join(file) for file in drive))


defragButton = tkinter.Button(master=window, text="Defrag", command=defrag)
defragButton.grid(column=1, row=2, **PADS)

outputText = tkinter.Text(master=window)
outputText.grid(column=1, row=3, columnspan=2, rowspan=3, **PADS)

outputText.insert("1.0", """
	Help: 
		- First input, then defrag, then display
		- Defrag again after removing corrupts
		- `X` represents a corrupt file
		- Defragged file is sent to `defragOut.txt`
""")


def display():
	global driveInfo
	toWrite = f"""{time.strftime("%H:%M:%S")}
File Map (after defrag)   : {" | ".join(driveInfo["fileMap"])}
File(length)            : {", ".join(f"{key}({driveInfo['lengths'][key]})" for key in sorted(driveInfo["files"]))}
\n"""
	outputText.insert(tkinter.END, toWrite)


printButton = tkinter.Button(master=window, text="Display", command=display)
printButton.grid(column=2, row=2, **PADS)


def removeCorrupts():
	global drive
	for index, line in enumerate(drive):
		if "Corrupt" in line:
			drive[index] = ["", ""]


removeButton = tkinter.Button(master=window, text="Remove Corrupts", command=removeCorrupts)
removeButton.grid(column=1, row=3, columnspan=2, **PADS)

tkinter.mainloop()
