"""A model to predict who would survive the titanic"""

import pandas
import numpy as np
import re

from collections import defaultdict

# Get data
DATA = pandas.read_csv("train.csv")
# Removing unneeded columns and empty boxes
for i in ["Ticket", "Cabin"]:
	del DATA[i]


# Set names to titles, use regex
def getTitle(name: str) -> str:
	# All titles in the file
	search = re.search(r"(\w+(?=\.))", name)
	return search.group()


DATA["Name"] = DATA["Name"].apply(getTitle)

# Give default age
DATA["Age"] = DATA["Age"].apply(lambda x: 30 if x == np.NAN else x)

# Now get rid of NaNs
DATA = DATA.dropna()

# Map other qualitative data to quantitative
maps = {"Sex": {"male": 0, "female": 1}, "Embarked": {"S": 0, "C": 1, "Q": 2}}
for i in maps.keys():
	DATA[i] = DATA[i].apply(lambda x: maps[i][x])

# Get averages for each header
AVERAGES = []
for column in DATA.columns:
	if column == "Name":
		# Most common as is qualitative
		AVERAGES.append(DATA[column].mode().values[0])
	else:
		AVERAGES.append(DATA[column].mean())

print(AVERAGES)

weights = defaultdict(lambda: 0)
# Iterate through rows and update weights
for passenger in DATA.iterrows():
	passenger = passenger[1]
	survived = passenger[1]
	for i in range(2, len(DATA.columns)):
		if i == 3:
			pass
		else:
			if survived:
				if passenger[i] > AVERAGES[i]:
					weights[i] += .1
				else:
					weights[i] -= .1

print(weights)
