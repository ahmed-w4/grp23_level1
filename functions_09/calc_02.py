# Sub programs
def add(a, b):
    c = a + b
    return c


def multiply(a, b, c):
    d = a * b * c
    return d


def absolute(x):
    if x < 0:
        y = x * -1
    else:
        y = x * 1
    return y


def divide(m, n):
    if n == 0:
       print('cannot divide by 0 ')
    else:
        o = m / n
        return o

# Main program starts
print('Program starts')
a = 7
b = 5
c = 9
d = -3
m = 15
n = 0
x = 17
y = 2
add_result = add(2, 6)
multi_result = multiply(a, m, y)
absolute_result = absolute(-3)
divide_result = round(divide(m, x), 2)

print(add_result)
print(multi_result)
print(absolute_result)
print(divide_result)

