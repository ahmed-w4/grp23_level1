# quadratic formula
# inputs

import math

a = 1
b = 5
c = 2
eq_1 = -b + math.sqrt(math.pow(b, 2) - 4 * a * c)
eq_2 = -b - math.sqrt(math.pow(b, 2) - 4 * a * c)
eq_3 = 2 * a
ans_1 = eq_1 / eq_3
ans_2 = eq_2 / eq_3


print(ans_1)
print(ans_2)