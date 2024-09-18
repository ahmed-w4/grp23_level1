# seeing if a num is in a list if not return -1
def check_num_found(my_list, num):
    if num in my_list:
        return my_list.index(num)
    else:
        return -1


data_list = [14, 17, 5, 2, 6]
var = 10321
checking_01 = check_num_found(data_list, var)  # Positional passing parameters
print(checking_01)

# named parameter
checking_02 = check_num_found(num=var, my_list=data_list)
print(checking_02)

print('test', end='')
data_list.sort(reverse=True)

print('omar', 'yahia', 'omnia', 'test', 'ola', 'ahmed')