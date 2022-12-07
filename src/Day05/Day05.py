import Read


data = Read.read_moves("input.txt")

stacks = Read.read_stacks("input_header.txt")

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
            for s in stacks:
                if s is stacks[m[2]-1]:
                    stacks[m[2]-1].insert(0, temp)
                else:
                    s.insert(0, None)
        else:
            llen = stacks[m[2]-1].__len__()
            while stacks[m[2]-1][j] is None:
                j = j + 1
                if j >= stacks[m[2]-1].__len__():
                    break
            if j != 0:
                j = j - 1
            stacks[m[2]-1][j] = temp
print(stacks)

out = ""
for s in stacks:
    for letter in s:
        if letter is not None:
            out = out + letter
            break

print(out)
