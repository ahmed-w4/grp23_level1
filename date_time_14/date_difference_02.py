# find difference between 2 dates
from datetime import datetime
# install package python-dateutil
from dateutil.relativedelta import relativedelta

today_1 = datetime.now()
custom_date = datetime(day=17, month=5, year=2022) # 17-May-2022

print('---- 1. difference in days -----')
difference = today_1 - custom_date
print(difference)
print(difference.days)


print('---- 2. difference in all parts year, months, days ... -----')
difference_parts = relativedelta(today_1, custom_date)
print(difference_parts)
print(difference_parts.years, difference_parts.months, difference_parts.days, difference_parts.microseconds)