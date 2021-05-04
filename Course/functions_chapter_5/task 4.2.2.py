string = input("Please enter your own String : ")

if(string == string[:: - 1]):
   print("This is a Palindrome String")
else:
   print("This is Not a Palindrome String")


# Task 4.2.4

import datetime
import calendar


date = input("enter a date in a format dd/mm/yyyy:")

DD = int(date [:2])

MM = int(date [3:5])

YYYY = int(date [6:])

day = calendar.weekday(YYYY, MM, DD)

print (calendar.day_name[day])
