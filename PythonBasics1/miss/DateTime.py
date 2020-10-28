#https://www.w3resource.com/python-exercises/date-time-exercise/
from datetime import datetime

now = datetime.now()

print(now)
print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))


print ("Current date : ")
print (now.strftime("%Y-%m-%d"))

#