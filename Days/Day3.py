import sys
wire1 = []
wire2 = []
intersects = []

with open('../Inputs/D3in.txt') as fp:
    line = fp.readline()
    for item in line.split(','):
        wire1.append(item)
    line = fp.readline()
    for item in line.split(','):
        wire2.append(item)


def mapper(wire):
    mapping = []
    x = 0
    y = 0
    total = 0
    for move in wire:
        num = int((move[1:]))
        if move[0] == 'R':
            for j in range(num):
                mapping.append((x + j, y, total + j))
            x += num
            total += num
        elif move[0] == 'L':
            for j in range(num):
                mapping.append((x - j, y, total + j))
            x -= num
            total += num
        elif move[0] == 'D':
            for j in range(num):
                mapping.append((x, y - j, total + j))
            y -= num
            total += num
        elif move[0] == 'U':
            for j in range(num):
                mapping.append((x, y + j, total + j))
            y += num
            total += num
    return mapping


map1 = mapper(wire1)
map2 = mapper(wire2)

print(len(map1))
print(len(map2))

d = {}

for m1 in map1:
    d[(m1[0], m1[1])] = m1[2]

for m2 in map2:
    if d.get((m2[0], m2[1])) is not None:
        thingy = (abs(m2[0]) + abs(m2[1]), m2[2] + d.get((m2[0], m2[1])))
        intersects.append(thingy[1])

minn = sys.maxsize
for i in intersects:
    if i < minn:
        if i != 0:
            minn = i

print(minn)
