# to add 2 years and 5 months and 20 days for today's day
from datetime import datetime
from dateutil.relativedelta import relativedelta

today_01 = datetime.now()
new_date = today_01 + relativedelta(years=2, months=5, days=20)
print(new_date.strftime('%d-%m-%Y'))

print('-------')
production_date = datetime(day=6, month=3, year=2024) # 14-3-2024
valid_months = 6
expired_date = production_date + relativedelta(months=valid_months)
print('The expired date for this product = ', expired_date.strftime('%d-%m-%Y'))
if today_01.date() <= expired_date.date():
    print('This product is still valid')
else:
    print('This product was expired')
print('-----')
warning_days = 10
difference = relativedelta(expired_date, today_01)
print(difference)
days_differ = difference.days + difference.months * 30 + difference.years * 365
print(days_differ)
if days_differ <= warning_days:
    print('Warning......')
else:
    print('No Warning yet')

