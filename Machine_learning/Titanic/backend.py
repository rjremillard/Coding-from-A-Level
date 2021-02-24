"""Creates tree for use in `frontend.py`"""

import pandas
import re
import numpy as np

from sklearn.tree import DecisionTreeRegressor


def makeModel(used_internally=False):
	""":param used_internally: whether it returns X and y"""
	# --- Constants ---
	TO_REMOVE = ["Ticket", "Cabin"]
	MAPS = {"Sex": {"male": 0, "female": 1}, "Embarked": {"S": 0, "C": 1, "Q": 2}}
	# TODO: Make names matter
	FEATURES = ["Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Embarked"]

	# --- Get and clean data ---
	data = pandas.read_csv("train.csv")
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

	# --- Process Data and Make Model ---
	# Get features and target
	y_ = data.Survived
	X_ = data[FEATURES]

	# Make model
	model_ = DecisionTreeRegressor(random_state=1)
	model_.fit(X_, y_)

	if used_internally:
		return model_, X_, y_
	else:
		return model_


# --- Sort Out the Rest ---
if __name__ == "__main__":
	# Get model and variables
	model, X, y = makeModel(used_internally=True)

	# Test the model
	test_return = model.predict(X)
	print(f"""
		Test results:
		
		Num of actual survivors:    {sum(y)}
		Num of predicted survivors: {round(sum(test_return))}
	""")
