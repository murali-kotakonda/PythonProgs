#import only class, function


from Module1 import Person
#from Module1 import *
from Module1 import Person,display1
#from pkg import <class>, <funtion>

from Module2 import performSum
#from pkg import  <funtion>

display1(899999)  # from Module1


sumRes = performSum(10,20) # from Module2
print(sumRes)


#Create obj for the class that exists in dif py file
p = Person()
p.id=3344
print(p.id)



