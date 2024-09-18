list = [1, 6, 3, 6, 3, 6]
num = 6
six_count = 0
for item in list:
    if item == num:
        six_count = six_count + 1

print('number 6 has appeared' ,six_count, 'times')