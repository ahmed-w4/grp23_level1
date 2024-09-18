def max_num(my_list):
    max = my_list[0]
    for number in my_list:
        if number > max:
            max = number
    return max


def min_num(my_list):
    min = my_list[0]
    for number in my_list:
        if number < min:
            min = number
    return min


my_list = [332, 632, 938210, 15820, -121, 200]
print('The max number is:', max_num(my_list))
print('The min number is:', min_num(my_list))