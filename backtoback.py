import pandas as pd 


df = pd.read_csv("basic_view.csv")

# convert Date column to datetime
df["Date"] = pd.to_datetime(df["Date"], format="%m/%d")  


# which team has the knicks beat the most 
df_wins = df[df["Result"] == "W"]
w_team_counts = df_wins["Opponent"].value_counts()
most_beaten_team = w_team_counts.index[0]

print(f"The Knicks have beaten {most_beaten_team} the most")

# which team has beaten the knicks the most 
df_wins = df[df["Result"] == "L"]
l_team_counts = df_wins["Opponent"].value_counts()
most_losses_aganist = w_team_counts.index[-1]

print(f"The Knicks have lost to {most_losses_aganist} the most")


# create new column showing if B2B games is going to happen with True being the first of the 2 games 
df["BackToBack"] = df["Date"].shift(-1) == df["Date"] + pd.Timedelta(1, "D")



# when games are played in two days consectuively, how many times have the knicks WON the second game
num_wins = df[(df["Result"] == "W") & (df["BackToBack"] == True)].count()[0]
# when games are played in two days consectuively, how many times have the knicks LOST the second game
num_losses = df[(df["Result"] == "L") & (df["BackToBack"] == True)].count()[0]


# the amount of back to back gamaes that have been played so far
num_games = df[(df["BackToBack"] == True) & (df["Result"].notnull())].count()[0]

# calculate the percentage of wins
percentage = num_wins / num_games * 100

# 1f formats the percentage to be to the 1 decimal point 
print(f"The Knicks have won {percentage:.1f}% of their back-to-back games.")

# when the result is W and the back to back is True, these values will be assigned to beaten_teams 
beaten_teams = df[(df["Result"] == "W") & (df["BackToBack"] == True)]["Opponent"]  
# only shows the team once 
beaten_teams_unique = beaten_teams.unique()
print(f"The Knicks beat {beaten_teams_unique} on B2B games")

# when the result is L and the back to back is True, these values will be assigned to lost_to_teams 
lost_to_teams = df[(df["Result"] == "L") & (df["BackToBack"] == True)]["Opponent"]  
# only shows the team once 
lost_teams_unique = lost_to_teams.unique()
print(f"The Knicks lost to {lost_teams_unique} on B2B games")


print(df)