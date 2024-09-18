
with open('C:\\my_files\\read_data.txt', 'r') as my_file:
    lines_list = my_file.readlines()
    new_lines_list = []
    for item in lines_list:
        item = item.strip()
        if item != '':
            new_lines_list.append(item)

    print(new_lines_list)