# Write a program to calculate the monthly income of a person using the
#following commission schedule:
''' Monthly sales income
>= Rs.50,000 Rs.375 + 16% sales.
>= Rs.50,000 but >=Rs.40,000 Rs. 350+14% sales.
<= Rs.40,000 but >=Rs.30,000 Rs. 325+12% sales.
<= Rs.30,000 but >=Rs.20,000 Rs. 300+9% sales.
<= Rs.20,000 but >=Rs.10,000 Rs. 250+5% sales.
<= Rs.10,000 Rs. 200+3% sales. '''

income = int(input("Enter Monthly Income: "))
income_commission = 0

if income >= 50000:
   income_commission = 375 + (income * 16) / 100
elif income <= 50000 and income >= 40000:
    income_commission = 350 + (income * 14) / 100
elif income <= 40000 and income >= 30000:
    income_commission = 325 + (income * 12) / 100
elif income <= 30000 and income >= 20000:
    income_commission = 300 + (income * 9) / 100
elif income <= 20000 and income >= 10000:
    income_commission = 250 + (income * 5) / 100
elif income <= 10000:
    income_commission = income + (200 + 3) / 100
print("Commission:", income_commission)