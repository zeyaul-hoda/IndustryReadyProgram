# Write a program to find whether the given numbers existing in an array or not.

array_no = (5,6,8,3,85,20)
a = int(input("Enter number to check in array: "))
if a in array_no:
    print("Number is existed in array")
else:
    print("Not Existed")