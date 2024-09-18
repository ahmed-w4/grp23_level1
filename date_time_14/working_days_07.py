# program to find the date after 12 working days from today
# ex: if today = 2-9-2024 - after 12 working days; will be [ 18-9-2024 ]
from datetime import datetime
from dateutil.relativedelta import relativedelta

today = datetime.now()
jump_days = 12

for i in range(jump_days):
    if today.weekday() == 3:
        today = today + relativedelta(days=3)
    elif today.weekday() == 4:  # Only to be checked the first round in the loop if today == Friday only
        today = today + relativedelta(days=2)
    else:
        today = today + relativedelta(days=1)
print(today)

