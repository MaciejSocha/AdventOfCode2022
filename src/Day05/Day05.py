import pandas as pd


data = pd.read_table("example.txt", header=None)
print(data)
with open('exmaple_header.txt') as lines:
    for line in lines.readlines():
        print(line)

