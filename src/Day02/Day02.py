import pandas as pd
import Methods


def main():
    data = pd.read_table("example.txt", header=None, delimiter=" ")
    for game in data.values:
        print(game)
        print(Methods.check_winning(game))


