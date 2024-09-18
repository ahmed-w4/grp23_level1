str_1 = 'cairoegypt'

half_1 = int(len(str_1)/2)

str_2 = str_1[0:half_1].lower()
str_3 = str_1[half_1:].upper()

new_str = str_2 + str_3
print(new_str)