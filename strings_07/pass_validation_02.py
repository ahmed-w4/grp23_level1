str_1 = "sr@m@_frtE$.321_"

count_lower = 0
count_upper = 0
count_num = 0
count_special = 0

if len(str_1) >= 8:
    for item in str_1:
        if item.islower():
            count_lower = count_lower + 1
        elif item.isupper():
            count_upper = count_upper + 1
        elif item.isdigit():
            count_num = count_num + 1
        elif not item.isalnum():
            count_special = count_special + 1
    if count_lower > 0 and count_upper > 0 and count_num > 0 and count_special > 0:
        print('strong password')
    else:
        print('invalid password try again')
else:
    print('Not valid - password should be >= 8 letters')

