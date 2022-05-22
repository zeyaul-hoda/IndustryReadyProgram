# Write a program to numbers divisible by 7 and multiple of 5, between 1 and 100.

for i in range(1, 100):
    if (i % 7 == 0 and i % 5 == 0):
        print(i)