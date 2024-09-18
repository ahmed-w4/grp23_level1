# create a sub program (function) named : print_numbers() to print numbers from min_num to max_num
#                   Then the function should return sum of these numbers
def print_numbers(min_num, max_num):
    total = 0
    for i in range(min_num, max_num + 1):
        print(i, end=' ')
        total = total + i
    print()
    return total

# main program
print('This is the main program')
total_1 = print_numbers(1, 10)     # 1 .. 10
print('-- Total = ', total_1)
total_2 = print_numbers(15, 20)    # 1 .. 20
print('-- Total = --', total_2)
total_3 = print_numbers(22, 25)     # 1 .. 25
print('-- Total = --', total_3)

q