normal_str = 'Hello world world Python is great great Python'
split_1 = normal_str.split()
unique_0 = []
duplicate_0 = []

for item in split_1:
    if item not in unique_0:
        unique_0.append(item)
    elif item not in duplicate_0:
        duplicate_0.append(item)

join_1 = ' '.join(unique_0)
print(join_1)