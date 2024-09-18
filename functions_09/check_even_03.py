# check if num is even return true if not return false
def check_even(num):
    """
    This function to check for even number and return True or False
    :param num: this is the parameter should be integer positive
    :return: True if the num is even , False if the num is odd
    """
    if num %2 == 0:
        return True
    else:
        return False


num = 8
is_even = check_even(num)

if is_even:
    print('This number is even', num)
else:
    print('This number isnt even', num)
