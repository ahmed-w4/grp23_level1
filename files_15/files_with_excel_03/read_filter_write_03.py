import csv

input_file = 'C:\\MY_FILES\\people1.csv'
output_file = 'C:\\MY_FILES\\people_filterred.csv'

with open(input_file, 'r') as read_from_file, open(output_file, 'w', newline='') as write_to_file:
    reader_list = csv.reader(read_from_file)
    writer_pen = csv.writer(write_to_file)
    writer_pen.writerow(['Name', 'Age', 'City'])
    for row in reader_list:
        if row[2] == 'Cairo':
            writer_pen.writerow(row)