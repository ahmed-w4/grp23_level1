dict1 = {'a': 100, 'b': 150, 'c': 100}
dict2 = {'a': 50, 'c': 100, 'd': 150}

for key in dict2:
    if key in dict1:        #  plus values  ( update )
        dict1[key] = dict1[key] + dict2[key]
    else:       # add new key
        dict1[key] = dict2[key]

print(dict1)