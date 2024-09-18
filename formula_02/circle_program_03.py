# to calc area and circumference of a circle
# inputs
import math

radius = 7.7

# processing
area = math.pi * math.pow(radius, 2)

circumference = 2 * math.pi * radius
# output
print('The area of circle is = ', round(area, 2))
print('The circumference is = ', round(circumference, 2))