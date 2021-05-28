"""
Get dates in diff format

%Y - year
%B - month full name
%b - month short hand notation
%d - date

%H : 24 hour

%I : 12  Hour

%M% : Minute
p : am/pm

solution:
for date formats use strftime() function


"""

from datetime import  datetime

currDate = datetime.now()
print("date = ",currDate)

print("Year = ", currDate.strftime("%Y"))

print("Month full name = ", currDate.strftime("%B"))

print("month = ", currDate.strftime("%b"))

print ("date style ",currDate.strftime("%d-%m-%Y %I:%M:%S  %p"))

print ("date style ",currDate.strftime("%d-%m-%Y %H:%M:%S  %p"))