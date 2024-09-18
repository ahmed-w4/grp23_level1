colours_list = [('red', 223), ('blue', 201), ('green', 210)]
dict_1 = {}

for key, value in colours_list:
    dict_1.setdefault(key, []).append(value)

print(dict_1)

for i in range(len(colours_list)):
    dict_1[colours_list[i][0]] = colours_list[i][1]
print(dict_1)

dict_test = dict(colours_list)
print(dict_test)