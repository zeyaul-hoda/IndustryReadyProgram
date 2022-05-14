# 6. Write a program to find the area and circumference of a circle.
from stringprep import in_table_c8


PI = 3.14
radius = int(input(' Please Enter the radius of a circle: '))

diameter = 2 * radius
circumference = 2 * PI * radius
area = PI * radius * radius

print(" \nDiameter Of a Circle = %.2f" %diameter)
print(" Circumference Of a Circle = %.2f" %circumference)
print(" Area Of a Circle = %.2f" %area)