code = []

with open('../Inputs/D2in.txt') as fp:
    line = fp.readline()
    for number in line.split(','):
        code.append(int(number))
while True:
    for noun in range(100):
        for verb in range(100):
            codes = code.copy()
            codes[1] = noun
            codes[2] = verb
            intCode = 0
            while True:
                if codes[intCode] == 1:
                    codes[codes[intCode + 3]] = codes[codes[intCode + 1]] + codes[codes[intCode + 2]]
                elif codes[intCode] == 2:
                    codes[codes[intCode + 3]] = codes[codes[intCode + 1]] * codes[codes[intCode + 2]]
                elif codes[intCode] == 99:
                    break
                else:
                    break
                intCode = intCode + 4
            if codes[0] == 19690720:
                print(100 * noun + verb)
    break;