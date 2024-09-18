# Here we will show all basic operations on datetime

# from datetime module import datetime class
from datetime import datetime
print('---- 1- get The current date and time ----')
today = datetime.now()
print(today)

print('---- 2- get only date or time or their parts ----')
print(today.time())
print(today.date())
print(today.date().day)
print(today.date().month)
print(today.date().year)
print(today.date().weekday()) # start with Monday = 0
print(today.time().hour)
print(today.time().minute)

print('-- 3- Reformatting date, time ------ | we use strftime() function-----')
print('----- Convert date into String using strftime() function ------')

print(today)
print(today.strftime('%d-%m-%Y'))   # day - month - YYYY
print(today.strftime('%d-%m-%Y-%y-%W'))   # day - month - YYYY - yy - week in year
print(today.strftime('%B-%b-%A-%a'))    # August - Aug - Monday - Mon

# format time
print(today.strftime('%H:%M-%S'))   # Hours 24 - Minutes - Seconds
print(today.strftime('%I:%M-%S %p')) # Hours 12 - Minutes - Seconds - pm


print('---- 4- Create a custom date 21-September-2023 ------')
print('---- 1st way : datetime object using constructor -------')
custom_date = datetime(day=21, month=9, year=2024)
print(custom_date.strftime('%d-%m-%Y'))

print('---- 2nd way : by converting a string into Date using strptime() function ----')
date_string_style = '9-13-2023' # string
new_custom_date = datetime.strptime(date_string_style, '%m-%d-%Y')
print(new_custom_date.strftime('%d-%m-%Y'))

print('------------ 5- Comparison ------------')
if today.date() > custom_date.date():
    print('today is greater than custom date')
elif custom_date.date() > today.date():
    print('custom date is greater than today')
else:
    print('both are same')
