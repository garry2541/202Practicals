# Practical 05
# Example 1: Datetime to string using strftime()

from datetime import datetime
now = datetime.now() # current date and time

year = now.strftime("%Y")
print("Year:",year)

month = now.strftime("%m")
print("Month:",month)

day = now.strftime("%d")
print("Day:",day)

time = now.strftime("%H:%M:%S")
print("Time:",time)

date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
print("Date and Time:",date_time)	