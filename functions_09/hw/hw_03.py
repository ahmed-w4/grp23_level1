def nums(num_01):
    for i in range(2, num_01):
        if num_01 % i == 0:
            return 'Not a prime number'
        else:
            return 'Prime number'

num_01 = 4
print(nums(num_01))