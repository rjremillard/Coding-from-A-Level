"""A model to predict who would survive the titanic"""

import pandas
import numpy as np
import re

from sklearn.tree import DecisionTreeRegressor


# --- Get and clean data ---
data = pandas.read_csv("train.csv")
# Removing unneeded columns and empty boxes
for i in ["Ticket", "Cabin"]:
	del data[i]

# # Set names to titles, use regex
# def getTitle(name: str) -> str:
# 	# All titles in the file
# 	search = re.search(r"(\w+(?=\.))", name)
# 	return search.group()
#
#
# data["Name"] = data["Name"].apply(getTitle)
#
# # Give default age
# data["Age"] = data["Age"].apply(lambda x: 30 if x == np.NAN else x)

# Now get rid of NaNs
data = data.dropna(axis=0)

# Map other qualitative data to quantitative
maps = {"Sex": {"male": 0, "female": 1}, "Embarked": {"S": 0, "C": 1, "Q": 2}}
for i in maps.keys():
	data[i] = data[i].apply(lambda x: maps[i][x])


# --- Process Data ---
# Get features and target
y = data.Survived

features = ["Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Embarked"]
X = data[features]
X.head()

model = DecisionTreeRegressor(random_state=1)
model.fit(X, y)

# Apply
print(X.head())
print(model.predict(X.head()))
