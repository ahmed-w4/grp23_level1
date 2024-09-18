import csv

with open("C:\\my_files\\people1.csv", 'r') as my_file:
    reader_list = csv.reader(my_file)
    counter = 0
    for row in reader_list:
        print(row)
        counter += 1

    print(counter - 1)

