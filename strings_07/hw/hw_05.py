num_1 = input('Enter a palindrome: ')

num_2 = num_1[::-1]
if num_2 == num_1:
    print('this is a palindrome')
else:
    print('this is not a palindrome')