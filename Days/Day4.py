count = 0


def check_number(n):
    d = {3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1}
    n = str(n)
    last_i = 0

    check = False
    for i in n:
        if int(i) < last_i:
            return False
        if int(i) == 0:
            return False
        if int(i) == last_i:
            d[int(i)] += 1
            check = True
        last_i = int(i)

    for i in range(9, 3, -1):
        if d[i] > 2:
            check = False
        elif d[i] == 2:
            return True
    return check


# for number in range(357253, 892942):
#     if check_number(number):
#         print(number)
#         count += 1

for number in range(357253, 400000):
    if check_number(number):
        count += 1

for number in range(444444, 500000):
    if check_number(number):
        count += 1

for number in range(555555, 600000):
    if check_number(number):
        count += 1

for number in range(666666, 700000):
    if check_number(number):
        count += 1

for number in range(777777, 800000):
    if check_number(number):
        count += 1

for number in range(888888, 892942):
    if check_number(number):
        count += 1

print(count)
