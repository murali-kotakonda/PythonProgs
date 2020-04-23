#https://www.w3resource.com/python-exercises/date-time-exercise/
import datetime
now = datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))

now = datetime.datetime.now()
print ("Current date : ")
print (now.strftime("%Y-%m-%d"))

#