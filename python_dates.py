## Python dates
# we can import a module named 'datetime' to work with dates as date objects
# the 'datetime' module has many methods to return information about the date object
import datetime

curr_date = datetime.datetime.now()
print(curr_date) # 2019-01-25 18:47:50.770067 | year-month-date hour:minute:second.microsecond
print(curr_date.year) # 2019
print(curr_date.strftime("%A")) # Friday

## Creating date objects
# use the datetime() class constructor
# datetime(year, month, day, hour, minute, second, microsecond, tzone)
# https://docs.python.org/3/library/datetime.html
ex_date = datetime.datetime(2020, 5, 17)
print(ex_date) # 2020-05-17 00:00:00, time defaults to zero
# the strftime() method can format a datetime based on the 'format' specified (ex. "%A", Weekday, full version)
# https://www.w3schools.com/python/python_datetime.asp
ex_date2 = datetime.datetime(2019, 1, 1)
print(ex_date2.strftime("%x")) # 01/01/19