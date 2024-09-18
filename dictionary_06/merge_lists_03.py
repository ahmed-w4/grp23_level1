emp_ids_list = [101, 102, 103]
emp_names_list = ['Ahmed', 'Omar', 'Sarah']

people_dict = {}

for i in range(len(emp_ids_list)):
    people_dict[emp_ids_list[i]] = emp_names_list[i]    # emp_ids_list[i] = 101
print(people_dict)

print('----------------------------')
people_dict = {}
names_idx = 0
for item in emp_ids_list:
    print(item)     # item = 101
    people_dict[item] = emp_names_list[names_idx]
    names_idx = names_idx + 1

print(people_dict)
