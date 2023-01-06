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


# Identify the minimum and maximum values in the Margin column
min_value = df["Margin"].min()
max_value = df["Margin"].max()

# Calculate the range of the data
range = max_value - min_value

# Normalize the Margin column
df["Normalized Margin"] = (df["Margin"] - min_value) / range

#Create the bar graph
counts.plot.bar()
plt.show()

