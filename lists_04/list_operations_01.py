# Using Lists
print('---- 1. Creating, Printing List ---- ')
my_list = [7, 9, 3, 15, 10]
print(my_list)
print(type(my_list))


print('------2. adding element to list [ append function , insert function ] --- ')
my_list.append(17)
my_list.insert(2, 6)
print(my_list)

print('---- 3. Access element by index and change it -----')
print(my_list[5])
my_list[5] = my_list[5] + 2
print(my_list)

print('----- 4. count elements of list _ Len function : General Function -------')
print(len(my_list))


print('-------- 5. delete element from the list -- remove() , pop() functions -----')
my_list.pop(2)
print(my_list)


print('-------- 6. reverse list ----------')
my_list.reverse()
print(my_list)

print('------- 7. sort list --- Asc , Desc ----------')
# my_list.sort()  # default Asc
# print(my_list)

my_list.sort(reverse= True)  # desc
print(my_list)