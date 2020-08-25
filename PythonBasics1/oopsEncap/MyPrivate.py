class PersonInfo:

    def __init__(self, pId, pName, pAge):
        self.__id = pId
        self.__name = pName
        self.__age = pAge
        # here __id , __name , __name are private [cannot access outside class]

    def show(self):
        print(self.id,self.name,self.age)

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


    def __str__(self):
        '''return "id =" + str(self.__id) +", nanme="+self.__name'''
        return "id={}, and name={}, age= {} , pan= {}".format(self.__id, self.__name,self.__age,self.pan)

myObj = PersonInfo(12000, "raj kumar", 34)




# access data
# print(myObj.age)
print(myObj.getAge())
# print(myObj.name)
print(myObj.getName())
# print(myObj.id)
print(myObj.getId())



print("******* change instance variables ********")
#myObj.id =90000
myObj.setId(90000)

#myObj.name="user89"
myObj.setName("user89")

#myObj.age=56
myObj.setAge(56)


print("after changing")
print(myObj.getAge())
print(myObj.getName())
print(myObj.getId())
