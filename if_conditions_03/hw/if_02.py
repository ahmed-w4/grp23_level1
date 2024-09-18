# give bonuses depending on the salary
# inputs
emp_salary = int(input("Enter your salary: "))

# processing and output
if emp_salary >= 5000:
    bonus = 2000
else:
    bonus = 4000

emp_salary = emp_salary + bonus
print("Your salary after bonus is $", emp_salary)
print('Bonus is = $', bonus)
