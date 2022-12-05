import pandas as pd
import Methods


data = pd.read_table("input.txt", header=None)

sums = 0
for line in data.values:
    half_len = int(len(line[0])/2)
    first_part = line[0][:half_len]
    second_part = line[0][half_len:]
    duplicates = [x for x in first_part if x in second_part]
    if duplicates[0].islower():
        sums = sums + Methods.calc_scoring_lower(duplicates[0])
    else:
        sums = sums + Methods.calc_scoring_upper(duplicates[0])

print(sums)



