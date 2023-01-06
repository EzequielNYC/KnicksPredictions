import pandas as pd 
import numpy as np
import matplotlib as plt

# basic view dataframe
df1 = pd.read_csv("basic.txt", sep='\t')

# Split the data in the first column into separate columns
df1 = df1['Date Opponent Result Score Location W/L Div'].str.split(expand=True)

# Rename the columns of the DataFrame
df1.columns = ['Date', 'Opponent', 'Result', 'Score', 'Location', 'W/L', 'Div']

# identifying rows in result which does not have W or L and assigns it to modify_result1
modify_result1 = df1.loc[~df1['Result'].isin(['W', 'L'])]

# using modify_result1 all values who do not have a W or L get replaced with NaN
df1.loc[modify_result1.index, 'Result'] = np.nan

# pm carried over to the score row, this removes all "pm" and replaces that with NaN
df1 = df1.replace('pm', np.nan)


# betting view dataframe
df2 = pd.read_csv("betting.txt", sep='\t')

# creating headers

# splitting this one string
df2 = df2['Date Opponent Result Score Spread Total Money'].str.split(expand=True)

# creating the column names, and addind total result for Pu(push) Ov(over) Un(under) on the total number of points
df2.columns = ['Date', 'Opponent', 'Result', 'Score', 'Spread','Total Result' ,'Total', 'Money']

#identifys all rows who do not contain W or L and assigns it to modify_result2
modify_result2 = df2.loc[~df2['Result'].isin(['W', 'L'])]
#using modify_result2 all values who do not have a W or L get replaced with NaN
df2.loc[modify_result2.index, 'Result'] = np.nan

# dropping pm which is in the score column 
df2 = df2.replace('pm', np.nan)

# Split the "score" column on the hyphen
df1[["Knicks", "opponent"]] = df1["Score"].str.split("-", expand=True)

# Fill missing values with 0 to turn each value into a int 
df1["Knicks"].fillna(0, inplace=True)
df1["opponent"].fillna(0, inplace=True)

# Convert the new columns to integers
df1["Knicks"] = df1["Knicks"].astype(int)
df1["opponent"] = df1["opponent"].astype(int)

# Drop the original "score" column
df1 = df1.drop(df1.columns[3], axis=1)

# creates a margin of victory column
df1['Margin'] = df1['Knicks'] - df1['opponent']


# turning DFs into CSVs
df1.to_csv('basic_view.csv', index=False)
df2.to_csv('betting_view.csv', index =False)

