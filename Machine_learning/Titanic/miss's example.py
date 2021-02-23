# pandas library is used in data science to explore and manipu;late data
# pandas uses a dataFrame, which is a bit like a table
import pandas as pd
# this library models data stored in dataframes
# define model, fit with data, predict and evaluate
from sklearn.tree import DecisionTreeRegressor

titanic_train = pd.read_csv("train.csv")
print(titanic_train.describe())
# drop missing values
titanic_train = titanic_train.dropna(axis=0)

print(titanic_train.describe())
# this gives 8 numbers for each column in dataset
# count  shows how many rows have non-missing values

# we need to see a list of columns:
print(titanic_train.columns)
# choose which one is the column we want to predict - this is y
y = titanic_train.Survived

# for a decision tree, all data must be numerical, using Pandas map() to change m/f
d = {"male": 0, "female": 1}
titanic_train["Sex"] = titanic_train["Sex"].map(d)

# then choose some features, that will be used to determine survival
titanic_features = ["Pclass", "Age", "Fare", "Sex"]

X = titanic_train[titanic_features]
# now we can use describe to review the data
print(X.describe())
# and the header, to see the first few rows
print("First rows of X", X.head())

# I added this in to check a couple of predictions visually - not necessary step
extra_features = ["PassengerId", "Survived"]
B = titanic_train[extra_features]
print("First rows of data:", B.head())

# now define the model
titanic_model = DecisionTreeRegressor(random_state=1)
# fit the model
titanic_model.fit(X, y)
# making predictions
print("Making predictions for the first 5 passengers:")
print(X.head())
print("The first 5 predictions are:")
print(titanic_model.predict(X.head()))

# then work it bigger
results = titanic_model.predict(X)

# output = pd.DataFrame({"PassengerId":pd.read_csv("train.csv").PassengerId, "Survived": results})
# output.to_csv("submission.csv", index=False)
