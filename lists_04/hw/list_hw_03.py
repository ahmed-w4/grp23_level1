# check if num is in the list
my_list = [1, 6, 3, 5, 3, 6, 6, 4, 6]
num = 6
number_found = False
for i in range(len(my_list)):
    if my_list[i] == num:
        number_found = True
        print('number is found in index', i)
        break    # to stop the loop

if not number_found:
    print('Number is not Found')

# task : print a list of all indexes of the occurrence of a number if found many times
#   [1, 5, 6, 8]
