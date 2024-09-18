# Program to show how to handle exceptions ( runtime errors)
import sys

try:
    first_number = int(input('PLease enter your first number '))
    second_number = int(input('PLease enter your second number '))

    result = first_number / second_number
    print('Result = ', result)
    open('c://my_files/employees.txt')
except ValueError as msg:
    print('PLease enter only numbers - ', msg)
    sys.exit()
except ZeroDivisionError as msg:
    print('cannot divide by 0 - ', msg)
    sys.exit()
# except Exception as msg:
#     print('Issue Happened - please contact administrator - 01012312312')
#     sys.exit()
finally:
    print('This finally code must work through any scenario')

print('End of the program')