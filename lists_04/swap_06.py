# to swap first and last numbers in the list
my_list = [6, 10, 7, 45, 19, 72]

temp = my_list[0]
my_list[0] = my_list[-1]
my_list[-1] = temp
print(my_list)
