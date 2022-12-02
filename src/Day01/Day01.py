df = []
temp = 0
with open('input.txt') as lines:
    for line in lines.readlines():
        if line != '\n':
            temp = temp + int(line)
        else:
            df.append(temp)
            temp = 0

df.sort(reverse=True)
print(df[0])
print((df[0] + df[1] + df[2]))
