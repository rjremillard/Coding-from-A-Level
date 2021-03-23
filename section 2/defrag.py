"""Goes over the data,
If corrupt - Leaves in place
Otherwise  - Attempts to arrange

Arranging steps:
	1. Find gaps where whole files can fit
	2. Attempt to clump files together
"""

import re
import tkinter

from tkinter import messagebox
from collections import defaultdict


# Get data
with open("defragIn.txt", "r") as f:
	drive = f.read().split("\n")
drive.append("END END")

# Map the drive
driveInfo = {
	"files": set(),
	"lengths": defaultdict(lambda: 0),
	"corruptMap": [],
	"gaps": []
}

gapCount, start = 0, 0
for index, line in enumerate(drive):
	file, fData = line.split()
	corrupt = not bool(re.match(r"[A-Z] [01]{8}$", line))

	# Add info
	driveInfo["files"].add(file)
	driveInfo["lengths"][file] += 1
	driveInfo["corruptMap"].append(corrupt)

	# Sort gaps
	if not corrupt:  # Normal file
		gapCount += 1
	else:
		if gapCount:
			driveInfo["gaps"].append({"length": gapCount, "span": (start, start + gapCount - 1)})
			gapCount = 0
		start = index + 1

# Try to move around

