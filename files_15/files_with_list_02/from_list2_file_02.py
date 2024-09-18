cities_list = ['cairo', 'alex', 'mansoura', 'aswan']

with open('C:\\my_files\\cities.txt', 'w') as my_file:
    for i in range(len(cities_list)):
        if i == len(cities_list)-1:
            my_file.write(cities_list[i])
        else:
            my_file.write(cities_list[i] + '\n')
