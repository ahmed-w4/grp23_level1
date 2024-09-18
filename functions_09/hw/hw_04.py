def sum_pos(list_01):
    sum_positive_numbers = 0
    for item in list_01:
        if item > 0:
            sum_positive_numbers = sum_positive_numbers + item
    return sum_positive_numbers


list_01 = [4, 5, 7, 15, -4, -6]
print('Thes sum of all positive numbers is :', sum_pos(list_01))


def count_pos(list_01):
    count_postive_nums = 0
    for item in list_01:
        if item > 0:
            count_postive_nums = count_postive_nums + 1
    return count_postive_nums


print('Total number of positive numbers is:', count_pos(list_01))