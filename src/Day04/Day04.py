import pandas as pd


data = pd.read_table("input.txt", header=None, delimiter=",")

elem = 0
for row in data.values:

    first = [x for x in range(int(row[0].split('-')[0]), int(row[0].split('-')[1])+1)]
    second = [x for x in range(int(row[1].split('-')[0]), int(row[1].split('-')[1])+1)]
    if any(x in first for x in second):
        elem = elem + 1
        print(second)
    else:
        if any(x in second for x in first):
            print(first)
            elem = elem + 1

print(elem)
