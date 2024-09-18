# read a file
"""
1- open file
2- read content
3- close file
"""
print('-- First way ---')
my_file = open('C:\\my_files\\read_data.txt', 'r')

content_1 = my_file.read()

print(content_1)

my_file.close()
print('-- Second way ---')

with open('C:\\my_files\\read_data.txt', 'r') as my_file:
    content_1 = my_file.read()
    print(content_1)