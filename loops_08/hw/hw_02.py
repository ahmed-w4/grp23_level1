result = ''
for i in range(1500, 2701):
    if i %5 == 0 and i %7 == 0:
        result = result + str(i) + ','

result = result[0:-1]
print(result)

