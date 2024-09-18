from datetime import datetime

dates_list = [datetime(2023, 12, 31), datetime(2023, 8, 15), datetime(2023, 5, 1)]
given_date = datetime(2023, 8, 15)

is_found = False
for item in dates_list:
    if given_date == item:
        print(given_date.date(), 'is found')
        is_found = True
if not is_found:
    print(given_date.date(), 'is not found')
