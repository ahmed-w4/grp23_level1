# program to write a list of lists to excel [ csv ] file
import csv

people_list = [
    ['Name', 'Age', 'City'],
    ['Adham', 25, 'Assuit'],
    ['Esam', 30, 'Cairo'],
    ['Shady', 28, 'Mansoura']
]


with open ('C:\\my_files\\people1.csv', 'w', newline='') as my_file:
    writer_pen = csv.writer(my_file)
    for row in people_list:
        writer_pen.writerow(row)
