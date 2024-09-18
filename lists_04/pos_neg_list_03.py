# total and el count of pos or neg numbers or zeros
my_list = [1, 17, 8, -5, 9, 0, -18, 0, 6.63, -3]
total_pos, total_neg, count_pos, count_neg, count_zeros = 0, 0, 0, 0, 0
for item in my_list:
    if item > 0:
        count_pos = count_pos + 1
        total_pos = total_pos + item
    elif item < 0:
        count_neg = count_neg + 1
        total_neg = total_neg + item
    else:
        count_zeros = count_zeros + 1

print('sum of positive numbers =', total_pos, 'count of positive numbers =', count_pos)
print('sum of negative numbers = ', total_neg, 'count of negative numbers =', count_neg)
print('count of zeros = ' , count_zeros)