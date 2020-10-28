#[ access display() in Module1 and access display() in Module2 ] using aliases
import  Module1 as m, Module2 as n
# import pkg1 as <alias1>,pkg2 as <alias1>

#access the global functions
m.display("hello")
n.display("hello")

#access global data
print(n.mylist)
print(n.user)
print(n.myTuple)
