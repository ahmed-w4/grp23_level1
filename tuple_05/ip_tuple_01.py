ip_tuple = [
    ('192.168.0.15', 'y'),
    ('192.168.0.22', 'y'),
    ('192.168.0.14', 'y'),
    ('192.168.0.24', 'n'),
    ('192.168.0.81', 'n'),
    ('192.168.0.115', 'y')

]
print(ip_tuple)
print(ip_tuple[2])
print(ip_tuple[2][0])
# loop over  the list and print only ips which has y value - and print the last part of ip
for item in ip_tuple:
    if item [1] == 'y':
        print(item[0])
        print(item[0][-2:])