#Write a program to find the G.C.D. of ‘n’ numbers.
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
s = 0
gcd = 0
if(a>b):
    s = b
else:
    s = a
for i in range(1,s+1):
    if(a % i == 0) and (b % i == 0):
        gcd = i
print(gcd)