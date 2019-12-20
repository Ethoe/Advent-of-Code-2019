import math
total = 0
with open('./Inputs/D1in.txt') as fp:
    line = fp.readline()
    while line:
        num = math.floor(int(line) / 3) - 2
        while num > 0:
            total = num + total
            num = math.floor(num / 3) - 2
        line = fp.readline()

print(total)
