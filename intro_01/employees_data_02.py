# program to show employee data
import math

emp_id = 101   # int data type
emp_name = 'Ahmed Wael'   # string data type
emp_salary = 7000.55   # float data type
emp_job = 'Python Developer'   # string
print('----- string concatenation --------')
print(emp_name + ' works as a ' + emp_job)

print('--------concat string with int -----')
print('--- Convert from int to str = Casting = convert from data type to another ----')
print(emp_name + ' id = ' + str(emp_id))

print('Emp: ' + emp_name + ' takes salary = ' + str(emp_salary))

print('----- Casting - convert from float to int ----- to remove decimal-----')
print(emp_salary)  # 7000.55

print(int(emp_salary))  # 7000   # casting = math.floor
print(math.ceil(emp_salary))  # 7001
print(round(emp_salary, 1))  # 7000.6
print(round(emp_salary))  # 7001
