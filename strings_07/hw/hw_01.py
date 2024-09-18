str_1 = 'A computer science portal for portal '

split_01 = str_1.split()

print(str_1.count('portal'))

count_no = 0
for item in split_01:
    if item == 'portal':
        count_no = count_no + 1

print(count_no)