print('1 = + \n2 = - \n3 = * \n4 = /')
# Ask the user for the operator
# inputs

operator = input("Enter the operator (1, 2, 3, 4): ")

# Ask the user for two values
value1 = float(input("Enter the first value: "))
value2 = float(input("Enter the second value: "))

# Calculate the result based on the operator
if operator == '1':
    result = value1 + value2
elif operator == '2':
    result = value1 - value2
elif operator == '3':
    result = value1 * value2
elif operator == '4':
    result = value1 / value2
else:
    print("Invalid operator entered!")
    result = None

# Print the result
if result is not None:
    print("Result: ", int(result))
