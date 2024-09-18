# add text to file

print('-- First way ---')
my_file = open('C:\\my_files\\write_data.txt', 'w')
my_file.write('I support Liverpool,\n\n')
my_file.write('\tI am Egyptian.')
my_file.close()



print('-- Second way ---')
with open('C:\\my_files\\write_data2.txt', 'w') as my_file:
    my_file.write('Hello again\n')
    my_file.write('Bye aagain')
