from datetime import datetime
from dateutil.relativedelta import relativedelta
dates_list = [datetime(2023, 12, 31), datetime(2023, 8, 15), datetime(2023, 5, 1)]

oldest_date = min(dates_list)
print(oldest_date.date())