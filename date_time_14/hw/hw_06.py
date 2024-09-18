from datetime import datetime
from dateutil.relativedelta import relativedelta

start_range = datetime(2023, 1, 1)
end_range = datetime(2023, 1, 10)

my_list = []
my_date = start_range
while my_date <= end_range:
      # print(my_date.date())
      my_list.append(my_date.date())
      my_date = my_date + relativedelta(days=1)
print(my_list)