# read and write to a file

with open('C:\\my_files\\read_data.txt', 'r') as my_file:
    content_1 = my_file.read()

with open('C:\\my_files\\write_data5.txt', 'w') as my_file2:
    my_file2.write(content_1.upper())

