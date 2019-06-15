# --------------
import numpy as np
# Read the data using numpy module

data_ipl = np.genfromtxt(path, delimiter=',', skip_header=1, dtype=str)

# Calculate the unique no. of matches in the provided dataset ?
data_ipl[:,3].shape

# Find the set of all unique teams that played in the matches in the data set.
# this exercise deals with you getting to know that which are all those six teams that played in the tournament.
team1_set = set(data_ipl[:, 3])
team2_set = set(data_ipl[:, 4])
unique_teams = team1_set.union(team2_set)

unique_teams

# Find sum of all extras in all deliveries in all matches in the dataset

# An exercise to make you familiar with indexing and slicing up within data.
extras = data_ipl[:, 17]
extras_int = extras.astype(np.int16)
extras_int.sum()

# Get the array of all delivery numbers when a given player got out. Also 
#mention the wicket type.

wicket_filter = (data_ipl[:, 20] == 'SR Tendulkar')
wickets_arr = data_ipl[wicket_filter]
wickets_arr[:, 11]

# How many matches the team Mumbai Indians has won the toss?

# this exercise will help you get the statistics on one particular team
team_records = data_ipl[data_ipl[:, 5] == 'Mumbai Indians']
unique_matches = set(team_records[:, 0])
len(unique_matches)

# Create a filter that filters only those records where the batsman scored 6 runs. Also who has scored the maximum no. of sixes overall ?

# An exercise to know who is the most aggresive player or maybe the scoring player 

sixes = data_ipl[data_ipl[:, 16].astype(np.int16) == 6]
from collections import Counter
most_sixes_scored = Counter(sixes[:,13],)
most_sixes_scored.most_common(3)




