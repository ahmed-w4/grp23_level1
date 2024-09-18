# find the nearest sunday
import calendar
from datetime import datetime
from dateutil.relativedelta import relativedelta

today = datetime.now()

print('----- Find the nearest sunday from today ----')
nearest_sunday = today + relativedelta(weekday=calendar.SUNDAY)
print(nearest_sunday.date())

print('----- Find the nearest 2nd sunday from today ----')
two_nearest_sunday = today + relativedelta(weekday=calendar.SUNDAY, days=7) # or weeks=1
print(two_nearest_sunday.date())
