# The task is to generate another list, which contains
# only unique elements and another contains the duplicate elements
my_list = [1, 2, 1, 2, 3, 4, 5, 1, 1, 2, 5, 6, 7, 8, 9, 9]
unique_list = []
duplicate_list =[]

for item in my_list:
    if item not in unique_list:
        unique_list.append(item)
    elif item not in duplicate_list:
        duplicate_list.append(item)
print(unique_list)
print(duplicate_list)
