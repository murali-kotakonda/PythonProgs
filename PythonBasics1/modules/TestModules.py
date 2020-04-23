import  Module1, Module2;

Module1.display("hello")
Module2.display("kumar")

#access gloabl of module2
print("module2222222222")
print(Module2.mylist)
print(Module2.user)
print(Module2.myTuple)

import  Module1 as m, Module2 as n;

m.display("hello")
n.display("hello")

from Module1 import Person
from Module1 import Person,display1
#from Module1 import *

p = Person()
p.id=3344
print(p.id)
display1(899999)
#display(89)


from Module2 import performSum

sumRes = performSum(10,20)
print(sumRes)



Module2.user ="shyam"
print(Module2.user)


Module2.mylist[0] = 'user5'
print(Module2.mylist)

