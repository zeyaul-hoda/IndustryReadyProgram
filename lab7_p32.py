#Write a program to read three sides a, b, c of a triangle and print the type of
#the triangle.
a = int(input("Enter first side of trianle:"))
b = int(input("Enter first side of trianle:"))
c = int(input("Enter first side of trianle:"))

if a == b and b == c:
    print("Equilateral Triagle")

elif a == b or b == c or c == a:
    print("Isoscales Triangle")
else:
    print("Scalene Triangle")