numbers = [10, 20, 35, 40, 50]
search_num = 22
found_01 = False
for num in numbers:
    if search_num == num:
        found_01 = True
        print('number is found in index: ', numbers.index(search_num))
        break

if found_01 == False:
    print('Not found')

