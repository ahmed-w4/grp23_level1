# get the sum and count of even and odd numbers
numbers_list = [15, 16, 20, 3, 9, 20]
even_count = 0
odd_count = 0
sum_even = 0
sum_odd = 0

for item in numbers_list:
    if item %2 == 0:
        even_count = even_count + 1
        sum_even = sum_even + item
    else:
        odd_count = odd_count + 1
        sum_odd = sum_odd + item

print(even_count, sum_even, odd_count, sum_odd)
