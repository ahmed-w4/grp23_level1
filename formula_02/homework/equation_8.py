# Loan equations
# inputs
import math

loanAmount = 100000
monthly_intrest_rate = 0.01
no_years = 7

monthlypayment_1 = loanAmount * monthly_intrest_rate
monthlypayment_2 = 1 - (1 / math.pow(1 + monthly_intrest_rate, no_years * 12))
ans = monthlypayment_1 / monthlypayment_2

print(round(ans, 2))

totalpayment = ans * no_years * 12
print(round(totalpayment, 2))
