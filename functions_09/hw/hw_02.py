def palin():
    num_1 = input('Enter a palindrome: ')
    num_2 = num_1[::-1]
    if num_2 == num_1:
        return True
    else:
        return False


print(palin())