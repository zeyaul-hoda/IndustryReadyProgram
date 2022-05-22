#Write a program to accept a date and print it in words

import datetime
dt_date = datetime.datetime.now()
print ("The Current date is:" ,dt_date)
print("In specified format:", dt_date.strftime("%A, %d %b %Y"))