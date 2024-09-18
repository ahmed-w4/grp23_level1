from datetime import datetime
start_date = datetime(2023, 1, 1)
end_date = datetime(2023, 1, 31)
given_date = datetime(2023, 1, 15)
#
# if given_date >= start_date and given_date <= end_date:
#     print(given_date, 'within range')
# else:
#     print(given_date.date(), 'Not in range')

if start_date <= given_date <= end_date:
    print(given_date.date(), 'within range')
else:
    print(given_date.date(), 'Not in range')