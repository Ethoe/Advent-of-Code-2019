import math
code = []

text = '../Inputs/D5in.txt'
with open(text) as fp:
    line = fp.readline()
    for number in line.split(','):
        code.append(int(number))

codes = code.copy()

intCode = 0
while True:
    opCode = codes[intCode] % 100
    if opCode == 1:
        vone = codes[intCode + 1] if math.floor(codes[intCode] / 100) % 10 else codes[codes[intCode + 1]]
        vtwo = codes[intCode + 2] if math.floor(codes[intCode] / 1000) % 10 else codes[codes[intCode + 2]]
        codes[codes[intCode + 3]] = vone + vtwo
        intCode += 4
    elif opCode == 2:
        vone = codes[intCode + 1] if math.floor(codes[intCode] / 100) % 10 else codes[codes[intCode + 1]]
        vtwo = codes[intCode + 2] if math.floor(codes[intCode] / 1000) % 10 else codes[codes[intCode + 2]]
        codes[codes[intCode + 3]] = vone * vtwo
        intCode += 4
    elif opCode == 3:
        print("Input value: ")
        codes[codes[intCode + 1]] = int(input())
        intCode += 2
    elif opCode == 4:
        vone = codes[intCode + 1] if math.floor(codes[intCode] / 100) % 10 else codes[codes[intCode + 1]]
        print(vone)
        intCode += 2
    elif opCode == 5:
        vone = codes[intCode + 1] if math.floor(codes[intCode] / 100) % 10 else codes[codes[intCode + 1]]
        vtwo = codes[intCode + 2] if math.floor(codes[intCode] / 1000) % 10 else codes[codes[intCode + 2]]
        intCode = vtwo if vone else intCode + 3
    elif opCode == 6:
        vone = codes[intCode + 1] if math.floor(codes[intCode] / 100) % 10 else codes[codes[intCode + 1]]
        vtwo = codes[intCode + 2] if math.floor(codes[intCode] / 1000) % 10 else codes[codes[intCode + 2]]
        intCode = intCode + 3 if vone else vtwo
    elif opCode == 7:
        vone = codes[intCode + 1] if math.floor(codes[intCode] / 100) % 10 else codes[codes[intCode + 1]]
        vtwo = codes[intCode + 2] if math.floor(codes[intCode] / 1000) % 10 else codes[codes[intCode + 2]]
        codes[codes[intCode + 3]] = 1 if vone < vtwo else 0
        intCode += 4
    elif opCode == 8:
        vone = codes[intCode + 1] if math.floor(codes[intCode] / 100) % 10 else codes[codes[intCode + 1]]
        vtwo = codes[intCode + 2] if math.floor(codes[intCode] / 1000) % 10 else codes[codes[intCode + 2]]
        codes[codes[intCode + 3]] = 1 if vone == vtwo else 0
        intCode += 4
    elif opCode == 99:
        print("Ended")
        break
    else:
        print("Broke")
        break

