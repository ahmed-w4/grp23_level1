# add all even nums together from a list
def even_sum(my_list):
    even_total = 0
    for item in my_list:
        if item %2 == 0:
            even_total = even_total + item
    return even_total


my_list = [14, 5, 7, 2, 6, 102]
result_sum = even_sum(my_list)
print(result_sum)