"""A model to predict who would survive the titanic"""

import pandas
import numpy as np

# Get data
DATA = pandas.read_csv("train.csv")
# Removing unneeded columns and empty boxes
for i in ["Name", "Ticket", "Cabin"]:
	del DATA[i]

# Give default age
DATA["Age"] = DATA["Age"].apply(lambda x: 30 if x == np.NAN else x)

# Now get rid of NaNs
DATA = DATA.dropna()

# Map other qualitative data to quantitative
maps = {"Sex": {"male": 0, "female": 1}, "Embarked": {"S": 0, "C": 1, "Q": 2}}
for i in maps.keys():
	DATA[i] = DATA[i].apply(lambda x: maps[i][x])

# Get averages for each header
AVERAGES = {}
for column in DATA.columns:
	AVERAGES[column] = DATA[column].mean()

print(AVERAGES)
