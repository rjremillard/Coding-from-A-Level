"""A model to predict who would survive the titanic"""

import pandas
import numpy as np
import re

from collections import defaultdict

# Between indexes and titles
IND_TITLE = {0: "PassengerId", 1: "Survived", 2: "Pclass", 3: "Name", 4: "Sex", 5: "Age", 6: "SibSp", 7: "Parch",
	8: "Fare", 9: "Embarked"}

# Get data
data = pandas.read_csv("train.csv")
# Removing unneeded columns and empty boxes
for i in ["Ticket", "Cabin"]:
	del data[i]


# Set names to titles, use regex
def getTitle(name: str) -> str:
	search = re.search(r"(\w+(?=\.))", name)
	return search.group()


data["Name"] = data["Name"].apply(getTitle)

# Give default age
data["Age"] = data["Age"].apply(lambda x: 30 if x == np.NAN else x)

# Now get rid of NaNs
data = data.dropna()

# Map other qualitative data to quantitative
maps = {"Sex": {"male": 0, "female": 1}, "Embarked": {"S": 0, "C": 1, "Q": 2}}
for i in maps.keys():
	data[i] = data[i].apply(lambda x: maps[i][x])


