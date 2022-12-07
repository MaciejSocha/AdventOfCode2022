import Read


data = Read.read_moves("example.txt")

stacks = Read.read_stacks("exmaple_header.txt")

print(data)
print(stacks)

for m in data.values:
    for i in range(1, m[0]+1):
        j = 0
        while stacks[m[1]-1][j] is None:
            j = j + 1
        temp = stacks[m[1]-1][j]
        stacks[m[1]-1][j] = None
        j = 0
        if stacks[m[2]-1][j] is not None:
            stacks[m[2]-1].append(temp)
            stacks[m[1]-1].append(None)
            stacks[m[0]-1].append(None)
        else:
            while stacks[m[2]-1][j] is None:
                j = j + 1
            j = j - 1
            stacks[m[2]-1][j] = temp
print(stacks)
