import csv
import matplotlib.pyplot as plt

with open("C:\\my_files\\people1.csv", 'r') as my_file:
    reader_list = csv.reader(my_file)
    reader_list.__next__()


    x = []
    y = []
    for item in reader_list:
        x.append(item[0])
        y.append(float(item[1]))
    print(x, y)

    plt.bar(x, y)
    plt.xlabel('Name')
    plt.ylabel('Age')
    plt.title('Peoples Ages')
    plt.xticks(rotation= 20)
    plt.show()