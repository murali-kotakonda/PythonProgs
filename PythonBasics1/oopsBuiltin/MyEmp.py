'''
Created on Jul 18, 2018

@author: I335484
'''

class MyClass:

    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age



myObj = MyClass(12000, "murali", 34)
# myObj.id=24
setattr(myObj, "id", 24)
# print myObj.id
print(getattr(myObj, "id"))


setattr(myObj, "name", "krish")

# print myObj.id
print(getattr(myObj, "name"))

print(hasattr(myObj, "name"))

