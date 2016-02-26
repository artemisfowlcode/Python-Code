# Display calendar of given month of the year
from os import system
# import module
import calendar


def say(var):
    system( 'say "%s"' % var)

# enter the month and year
say("Please Enter year")
year = int(input("Enter year: "))
say("Please Enter month")
month = int(input("Enter month: "))

# display the calendar

print(calendar.month(year,month))
