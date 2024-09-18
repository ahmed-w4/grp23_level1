# This to show how to loop on a list
my_list = [7, 9, 6, 3, 15, 10, 17]

print('--- 1- loop using for i loop ---- this will use the index ---')
total = 0
for i in range(len(my_list)):
    print(my_list[i])
    total = total + my_list[i]
print('total of elements = ', total)
average = total / len(my_list)
print('average of elements = ', round(average, 2))

print('---- 2- loop using for each loop --- this will not use the index -----')
total = 0
for item in my_list:
    print(item)     # my_list[i]
    total = total + item
print('total of elements = ', total)
average = total / len(my_list)
print('average of elements = ', round(average, 2))


print('--- 3- total using built in function sum ----')
print(sum(my_list))



