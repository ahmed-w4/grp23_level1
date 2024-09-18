from datetime import datetime
from dateutil.relativedelta import relativedelta

dates_list = [
    datetime(2023, 12, 31),
    datetime(2023, 12, 15),
    datetime(2023, 12, 15),
    datetime(2023, 12, 1)
]
month_1 = dates_list[0].month
print(month_1)

is_found = True

for date in dates_list:
    if date.month != month_1:
        is_found = False

if not is_found:
    print('not all dates are in the same month')
else:
    print('all dates are in the same month')





