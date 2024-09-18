from datetime import datetime
from dateutil.relativedelta import relativedelta

dates_list = [
    datetime(2023, 12, 31),
    datetime(2023, 8, 15),
    datetime(2023, 8, 15),
    datetime(2023, 5, 1)
]
given_date = datetime(2023, 8, 15)

count_given = 0
for item in dates_list:
    if item == given_date:
        count_given = count_given + 1

print(given_date.date(), 'has appeared', count_given, 'times')