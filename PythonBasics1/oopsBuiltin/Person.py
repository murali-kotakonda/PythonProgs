'''
Created on Jul 18, 2018

@author: I335484
'''

class Person:
    id =None
    name = None
    age = None


#create obj
myObj = Person()


#set datA
setattr(myObj, "id", 24000)
setattr(myObj, "name", "user1")
setattr(myObj, "age", 24)


# print DATA
print(getattr(myObj, "id"))
print(getattr(myObj, "name"))
print(getattr(myObj, "age"))


setattr(myObj, "name", "krish")

# print myObj.id
print(getattr(myObj, "name"))

print(hasattr(myObj, "name"))

