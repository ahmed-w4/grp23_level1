numbers = [10, 20, 35, 40, 50]
search_num = 40
for num in numbers:
    if search_num == num:
        print('number is found in index: ', numbers.index(search_num))
        break
else:
    print('Number is not found')