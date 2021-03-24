"""Goes over the drive,
gathers info,
and bubble sorts the files (most efficient sort for this purpose)

Gives the user the option to either delete or inspect any corrupt files
"""

import re
import tkinter

from tkinter import messagebox
from collections import defaultdict


# Get data
with open("defragIn.txt", "r") as f:
	drive = [line.split() for line in f.read().split("\n")]

# Get drive info
driveInfo = {
	"files": set(),
	"lengths": defaultdict(lambda: 0),
	"fileMap": []
}

gapCount, start = 0, 0
for index, line in enumerate(drive):
	file, fData = line
	corrupt = not bool(re.match(r"[A-Z] [01]{8}$", " ".join(line)))

	# Sort corrupt files
	if corrupt:
		drive[index].append("Corrupt")

	# Add info
	driveInfo["files"].add(file)
	driveInfo["lengths"][file] += 1
	driveInfo["fileMap"].append("X" if corrupt else file)

# Sort
swapped, n = True, 1
while swapped:
	swapped = False
	for i in range(len(drive) - n):
		if drive[i] > drive[i+1]:
			drive[i], drive[i+1] = drive[i+1], drive[i]
			swapped = True

print(*[i[0] if len(i)==2 else "Corrupt" for i in drive], sep="|")
print(*drive, sep="\n")
