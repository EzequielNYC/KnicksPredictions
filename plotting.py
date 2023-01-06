# seeing the margins points the Knicks win or lose by

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


df = pd.read_csv("basic_view.csv")

# Create bins for the margins of victory, excluding 0s
bins = pd.cut(df[df["Margin"] != 0]["Margin"], bins=range(-30, 45, 5))

# Group the data by the bins and count the number of rows in each group
counts = df[df["Margin"] != 0].groupby(bins).size()

#Create the bar graph
#counts.plot.bar()
#plt.show()


# Identify the minimum and maximum values in the Margin column
min_value = df["Margin"].min()
max_value = df["Margin"].max()

# Calculate the range of the data
range = max_value - min_value

# Normalize the Margin column
df["Normalized Margin"] = (df["Margin"] - min_value) / range



"""
# Extract the Normalized Margin and Result columns from the dataframe
X = df[["Normalized Margin"]]
y = df["Result"]

# Convert the Result column to a binary outcome (win or loss)
y = np.where(y == "W", 1, 0)

# Split the data into a training set and a test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train a random forest classifier on the training data
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Make predictions on the test data
y_pred = model.predict(X_test)

# Calculate the accuracy of the model
accuracy = accuracy_score(y_test, y_pred)

print("Accuracy:", accuracy)
"""