# to verify age of user
# inputs
age = int(input('What is your age? ' ))

# processing and output
if age > 100:
    print("You're way too old")
elif age > 16:
    print("You're a man")
elif age >= 11:
    print("You're a boy")
elif age < 0:
    print("You're not even born yet")
else:
    print("You're a child")