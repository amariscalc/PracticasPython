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
