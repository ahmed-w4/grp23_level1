# This program is to check if there are no reminders once dividing
List_numbers = [10, 15, 20, 45, 60, 30, 17]

for item in List_numbers:
    if item % 3 == 0 and item % 5 == 0:
        print(item)
        