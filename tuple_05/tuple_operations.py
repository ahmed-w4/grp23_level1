print('---- create and print tuple -----')
my_tuple = (101, 'Ahmed', 50000, 'cairo')

print(my_tuple)
print(type(my_tuple))




print('---------- access element in a tuple by index -------------')
print(my_tuple[2])


print('------------ un packing tuple ----- ')
id_01, name_02, salary_03, address_04 = my_tuple
print(id_01, name_02, salary_03, address_04)


print('------ Loop over Tuple -------')
for i in range(len(my_tuple)):
    print(my_tuple[i])

for item in my_tuple:
    print(item)