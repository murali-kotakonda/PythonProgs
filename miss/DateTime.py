#https://www.w3resource.com/python-exercises/date-time-exercise/
import datetime
now = datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))


# 
# 1. Write a Python script to display the - Go to the editor
# a) Current date and time
# b) Current year
# c) Month of year
# d) Week number of the year
# e) Weekday of the week
# f) Day of year
# g) Day of the month
# h) Day of week

import time
import datetime
print("Current date and time: " , datetime.datetime.now())
print("Current year: ", datetime.date.today().strftime("%Y"))
print("Month of year: ", datetime.date.today().strftime("%B"))
print("Week number of the year: ", datetime.date.today().strftime("%W"))
print("Weekday of the week: ", datetime.date.today().strftime("%w"))
print("Day of year: ", datetime.date.today().strftime("%j"))
print("Day of the month : ", datetime.date.today().strftime("%d"))
print("Day of week: ", datetime.date.today().strftime("%A"))




#program to convert a string to datetime.
from datetime import datetime
date_object = datetime.strptime('Jul 1 2014 2:43PM', '%b %d %Y %I:%M%p')
print(date_object)



#program to get the current time.
import datetime
print(datetime.datetime.now().time())


#program to subtract five days from current date.
from datetime import date, timedelta
dt = date.today() - timedelta(5)
print('Current Date :',date.today())
print('5 days before Current Date :',dt)

#n program to print yesterday, today, tomorrow.
import datetime 
today = datetime.date.today()
yesterday = today - datetime.timedelta(days = 1)
tomorrow = today + datetime.timedelta(days = 1) 
print('Yesterday : ',yesterday)
print('Today : ',today)
print('Tomorrow : ',tomorrow)


#print next 5 days starting from today.
import datetime
base = datetime.datetime.today()
for x in range(0, 5):
      print(base + datetime.timedelta(days=x))
#week no
print(datetime.date(2015, 6, 16).isocalendar()[1])



#convert a string date to the timestamp.
import time
import datetime
s = "01/10/2016"
print()
print(time.mktime(datetime.datetime.strptime(s, "%d/%m/%Y").timetuple()))
print()

      

