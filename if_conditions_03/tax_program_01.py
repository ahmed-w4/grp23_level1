# to get net salary after taxation
# inputs
emp_gross_salary = 100000

# processing
if emp_gross_salary >= 5000:
   tax = 10
else:
   tax = 0

emp_net_salary = emp_gross_salary - tax/100 * emp_gross_salary

# output
print("The employee's net salary is $ ", emp_net_salary)
print(tax, '%')