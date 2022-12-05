import pandas as pd
import Methods

data = pd.read_table("input.txt", header=None, delimiter=" ")
score = 0
for game in data.values:
    score = score + Methods.check_winning(game) + Methods.give_points(game[1])
print(score)
