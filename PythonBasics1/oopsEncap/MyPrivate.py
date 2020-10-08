"""


Req:
- Create person class with id, name , age as instance variables.
-  id, name , age are private
- provide setters and getters
- create object and set the data and print the data
"""

class PersonInfo:

    def __init__(self, pId, pName, pAge):
        self.__id = pId
        self.__name = pName
        self.__age = pAge
        # here __id , __name , __name are private [cannot access outside class]

    def show(self):
        print(self.__id,self.__name,self.__age)

   #provide the setter and getter methods
    # 3 setters and 3 getters
    # for changing or accesisng use the methods
    def getName(self):
        return self.__name

    def setName(self, name):
         self.__name = name
        
    def getId(self):
        return self.__id

    def setId(self, id):
         self.__id = id

    def getAge(self):
        return self.__age

    def setAge(self, age):
         self.__age = age



p = PersonInfo(1200,"USER2",23)

#change id
p.setId(1300)
print(p.getId())

#change name
p.setName("Raj")
print(p.getName())

#change age
p.setAge(78)
print(p.getAge())

print("**************")
p.show()