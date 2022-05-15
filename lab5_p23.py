#Write a program to read the marks of 3 subjects and display the total, average, class.

a = int(input("Enter first subject marks:"))
b = int(input("Enter second subject marks:"))
c = int(input("Enter third subject marks:"))
total = a + b + c 
avg = total / 3
print("Total marks:", total)
print("Average marks:", avg)