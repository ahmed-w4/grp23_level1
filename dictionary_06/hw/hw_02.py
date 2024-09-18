tuple_01 = (101, 'Ahmed', 5000.0, 'Cairo', 30234700)
tuple_02 = (102, 'Mohamed', 4500.0, 'ALex', 113121411)
tuple_03 = (103, 'Omar', 4000.0, 'El Sahel', 222738222)

persons_values_tuple = (tuple_01, tuple_02, tuple_03)
person_names_tuple = ('person1', 'person2', 'person3')
dict_01 = {}

for i in range(len(persons_values_tuple)):
    dict_01[person_names_tuple[i]] = persons_values_tuple[i]
print(dict_01)