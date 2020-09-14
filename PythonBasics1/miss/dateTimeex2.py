# 1. Write a Python script to display the - Go to the editor
# a) Current date and time
# b) Current year
# c) Month of year
# d) Week number of the year
# e) Weekday of the week
# f) Day of year
# g) Day of the month
# h) Day of week
"""
%Y - year
%B - month full name
%b - month short hand notation
%d - date

%H : 12 hour

%I : 24  Hour

%M% : Minute
p : am/pm


%Y-%m-%d %H:%M:%S



Directive	Meaning	Example
%a	Abbreviated weekday name.	Sun, Mon, ...
%A	Full weekday name.	Sunday, Monday, ...
%w	Weekday as a decimal number.	0, 1, ..., 6
%d	Day of the month as a zero-padded decimal.	01, 02, ..., 31
%-d	Day of the month as a decimal number.	1, 2, ..., 30
%b	Abbreviated month name.	Jan, Feb, ..., Dec
%B	Full month name.	January, February, ...
%m	Month as a zero-padded decimal number.	01, 02, ..., 12
%-m	Month as a decimal number.	1, 2, ..., 12
%y	Year without century as a zero-padded decimal number.	00, 01, ..., 99
%-y	Year without century as a decimal number.	0, 1, ..., 99
%Y	Year with century as a decimal number.	2013, 2019 etc.
%H	Hour (24-hour clock) as a zero-padded decimal number.	00, 01, ..., 23
%-H	Hour (24-hour clock) as a decimal number.	0, 1, ..., 23
%I	Hour (12-hour clock) as a zero-padded decimal number.	01, 02, ..., 12
%-I	Hour (12-hour clock) as a decimal number.	1, 2, ... 12
%p	Locale’s AM or PM.	AM, PM
%M	Minute as a zero-padded decimal number.	00, 01, ..., 59
%-M	Minute as a decimal number.	0, 1, ..., 59
%S	Second as a zero-padded decimal number.	00, 01, ..., 59
%-S	Second as a decimal number.	0, 1, ..., 59
%f	Microsecond as a decimal number, zero-padded on the left.	000000 - 999999
%z	UTC offset in the form +HHMM or -HHMM.
%Z	Time zone name.
%j	Day of the year as a zero-padded decimal number.	001, 002, ..., 366
%-j	Day of the year as a decimal number.	1, 2, ..., 366
%U	Week number of the year (Sunday as the first day of the week). All days in a new year preceding the first Sunday are considered to be in week 0.	00, 01, ..., 53
%W	Week number of the year (Monday as the first day of the week). All days in a new year preceding the first Monday are considered to be in week 0.	00, 01, ..., 53
%c	Locale’s appropriate date and time representation.	Mon Sep 30 07:06:05 2013
%x	Locale’s appropriate date representation.	09/30/13
%X	Locale’s appropriate time representation.	07:06:05
%%	A literal '%' character.	%
"""
import time
import datetime

from datetime import datetime

now = datetime.now()

print("Current date and time: ",  now)
print("Current date format: ", now.strftime("%Y/%B/%d  %I:%M%p"))
print("Current year: ", now.strftime("%Y"))
print("Month of year: ",now.strftime("%B"))
print("Month of year: ", now.strftime("%b"))
print("Week number of the year: ", now.strftime("%W"))
print("Weekday of the week: ",now.strftime("%w"))
print("Day of year: ", now.strftime("%j"))
print("Day of the month : ", now.strftime("%d"))
print("Day of week: ", now.strftime("%A"))
print("Day of week: ", now.strftime("%a"))
print("Time: ", now.time())


print("************************string to datetime.**********************************")
# program to convert a string to datetime.
"""
strftime -> obj to str
strptime -> str to obj
"""
from datetime import datetime
dateStr= 'Jul 1 2014 2:43PM'
date_object = datetime.strptime(dateStr, '%b %d %Y %I:%M%p')
print(date_object)


print("*********** timestamp to date **********************")
from datetime import datetime

timestamp = 1528797322
date_time = datetime.fromtimestamp(timestamp)

print("Date time object:", date_time)

d = date_time.strftime("%m/%d/%Y, %H:%M:%S")
print("Output 2:", d)

d = date_time.strftime("%d %b, %Y")
print("Output 3:", d)

d = date_time.strftime("%d %B, %Y")
print("Output 4:", d)

d = date_time.strftime("%I%p")
print("Output 5:", d)

print("************************program to print yesterday, today, tomorrow.**********************************")
# n program to print yesterday, today, tomorrow.
import datetime

today = datetime.date.today()
yesterday = today - datetime.timedelta(days=1)
tomorrow = today + datetime.timedelta(days=1)
dt = today - datetime.timedelta(5)

print('Yesterday : ', yesterday)
print('Today : ', today)
print('Tomorrow : ', tomorrow)
print('5 days before Current Date :', dt)

print("************************print next 5 days starting from today.**********************************")
# print next 5 days starting from today.
import datetime

base = datetime.datetime.today()
for x in range(0, 5):
    print(base + datetime.timedelta(days=x))
# week no
print(datetime.date(2015, 6, 16).isocalendar()[1])

print("************************convert a string date to the timestamp.**********************************")
# convert a string date to the timestamp.
import time
import datetime

s = "01/10/2016"
print()
print(time.mktime(datetime.datetime.strptime(s, "%d/%m/%Y").timetuple()))
print()



