# 9. Write a program to find your age in days.

from datetime import datetime  # imports datetime package
date_of_birth = datetime(1997, 12, 9) 
count_days = datetime.today() - date_of_birth
print (f'Your Age in Days are {count_days.days}')  #  printing age in days