"""A model to predict who would survive the titanic"""

import pandas
import re
import tkinter
import numpy as np

from sklearn.tree import DecisionTreeRegressor


# --- Constants ---
FILE_PATH = "train.csv"
TO_REMOVE = ["Ticket", "Cabin"]
MAPS = {"Sex": {"male": 0, "female": 1}, "Embarked": {"S": 0, "C": 1, "Q": 2}}
FEATURES = ["Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Embarked"]

# --- Tkinter start ---
window = tkinter.Tk()
window.title = "Who Will Survive?"

title = tkinter.Label(master=window, text="Titanic - who will survive?")

# --- Get and clean data ---
data = pandas.read_csv(FILE_PATH)
# Removing unneeded columns and empty boxes
for i in TO_REMOVE:
	del data[i]


# Set names to titles, use regex
def getTitleNum(name: str) -> str:
	# All titles in the file
	search = re.search(r"(\w+(?=\.))", name)
	return search.group()


data["Name"] = data["Name"].map(getTitleNum)

# Give default age
data["Age"] = data["Age"].map(lambda x: 30 if x == np.NAN else x)

# Now get rid of NaNs
data = data.dropna(axis=0)

# Map other qualitative data to quantitative
for i in MAPS.keys():
	data[i] = data[i].map(lambda x: MAPS[i][x])


# --- Process Data ---
# Get features and target
y = data.Survived

X = data[FEATURES]
X.head()

model = DecisionTreeRegressor(random_state=1)
model.fit(X, y)

# Apply
predictions = model.predict(X)

print(f"""
	Actual survived:    {data.Survived.sum()}
	Predicted survived: {sum(predictions)}
""")

print(model.feature_importances_)
