#[ access display() in Module1 and access display() in Module2 ]

import  Module1, Module2
# import pkg1,pkg2

#access the global functions

Module1.display("hello")
Module2.display("kumar")

#access global data
print(Module2.mylist)
print(Module2.user)
print(Module2.myTuple)
