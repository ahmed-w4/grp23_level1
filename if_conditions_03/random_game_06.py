# random num game
# inputs
import random

frstnum = random.randint(1, 100)
secnum = random.randint(1, 100)

# processing
print(frstnum, '+', secnum, '=')
usr_ans = int(input(''))
if usr_ans == frstnum + secnum:
    print('correct answer')
else:
    print('wrong answer')