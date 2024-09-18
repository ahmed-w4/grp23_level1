ips_List = [
    ('192.168.0.15', 'y'),
    ('192.168.0.22', 'y'),
    ('192.168.0.14', 'y'),
    ('192.168.0.24', 'n'),
    ('192.168.0.15', 'y'),
    ('192.168.0.11', 'y')
]
unique_ip = []
duplicate_ip = []
for item in ips_List:
    if item not in unique_ip:
        unique_ip.append(item)
    else:
        duplicate_ip.append(item)
print(unique_ip)
