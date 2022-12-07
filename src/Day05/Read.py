import pandas as pd


def read_moves(file: str) -> pd.DataFrame:
    data = pd.read_table(file, header=None, sep=r"move|from|to", engine='python')
    data = data.drop(columns=0)
    return data


def read_stacks(file: str) -> [[]]:
    with open(file) as lines:
        last_line = lines.readlines()[-1]
    last_number = int(last_line[-1])
    stacks = [[] for x in range(1, last_number + 1)]

    with open(file) as lines:
        for line in lines.readlines():
            if line[:2] == " 1":
                break
            i = 0
            for c in range(len(stacks)):
                if line[:3] == "   ":
                    line = line[4:]
                    stacks[i].append(None)
                else:
                    if line == '\n':
                        stacks[i].append(None)
                    else:
                        if line[:1] == " ":
                            temp_line = line[2:]
                            stacks[i].append(temp_line[:1])
                            line = line[4:]
                        else:
                            temp_line = line[1:]
                            stacks[i].append(temp_line[:1])
                            line = line[3:]
                i = i + 1
    return stacks
