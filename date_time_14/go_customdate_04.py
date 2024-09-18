# got first day of month and last day
from datetime import datetime
from dateutil.relativedelta import relativedelta

today_01 = datetime.now()
month_now = today_01.strftime('%B')

first_day = today_01 + relativedelta(day=1)
last_day = today_01 + relativedelta(day=31)

print('First day of', month_now, first_day.date())
print('Last day of', month_now, last_day.date())

