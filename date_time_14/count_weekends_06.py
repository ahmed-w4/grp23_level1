# count no of weekends in a month
from datetime import datetime
from dateutil.relativedelta import relativedelta

y = 2024
m = 11
custom_date = datetime(year=y, month=m, day=1)

print(custom_date.date())
# end_date = datetime(day=30, month=m, year=y)
end_date = custom_date + relativedelta(day=31)
count = 0
print(end_date.date())

while custom_date <= end_date:
    if custom_date.weekday() == 4 or custom_date.weekday() == 5:
        count = count + 1
        # print('Friday or saturday', custom_date)
    # print(custom_date)
    custom_date = custom_date + relativedelta(days=1)
print(count)
