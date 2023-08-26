# dates

'''
A date in Python is not a data type of its own, 
but we can import a module named datetime to work with dates as date objects.

More info:
https://www.w3schools.com/python/python_datetime.asp#:~:text=A%20date%20in%20Python%20is,with%20dates%20as%20date%20objects.
'''

# Import the class "datetime" of the module "datetime".
'''
The datetime module supplies classes for manipulating dates and times. 
While date and time arithmetic is supported, 
the focus of the implementation is on efficient attribute extraction for output formatting and manipulation.
'''
from datetime import datetime
from datetime import date
from datetime import time

# Import module month_name
import calendar

def today (now):
    
    print ("Today is %s %dth of the year %d " %(calendar.month_name[now.month],now.day,now.year))
    
def day_week(now):

    #today = list ()
    #day_numb = datetime.weekday(now)
    
    # Get the day´s name
    #today = calendar.day_name

    # Print the today name
    #print ("Today is %s " %(today[(day_numb)]))

    #return today[(day_numb)]
    
    return calendar.day_name[(datetime.weekday(now))]

# Get current datetime
now = datetime.now()

# What is today?
today (now)

# Get that day is today
day_week_get = day_week(now)
print (day_week_get)

# print hour, minute, second....
print (now.hour)
print (now.minute)
print (now.second)
print (now.year)
print (now.month)
print (now.day)

# timestamp 
'''
imestamp is the date and time of occurrence of an event. 
In Python we can get the timestamp of an event to an accuracy of milliseconds. 
The timestamp format in Python returns the time elapsed from the epoch time which is set to 00:00:00 UTC 
for 1 January 1970.
'''
print (datetime.timestamp(now))

# Set a new date
year_2023 = datetime(year=2023,month=1,day=1) # 2023-01-01 00:00:00
print ("...",datetime.timetz(now))

new_year_2023 = datetime (2023,1,1,00,00,00,1)
print (new_year_2023) # 2023-01-01 00:00:00.000001

# ctime
now_date = date (2023,1,1)
print (now_date.ctime()) # Sun Jan  1 00:00:00 2023

print (now_date.fromisocalendar(2023,35,3)) # 2023-08-30

print (now_date.replace(year=2024)) # 2024-01-01

# Empyt constructor 
my_time = time ()
print (my_time) # 00:00:00

# New values to "my_time" (or another variable) 
my_time = my_time.replace(12,00,1)
print (my_time) # 12:00:01
