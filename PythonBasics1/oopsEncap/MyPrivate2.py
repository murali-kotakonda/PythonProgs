class PersonInfo:

    def __init__(self, pId, pName, pAge, pPan):
        self.__id = pId
        self.__name = pName
        self.__age = pAge
        self.pan = pPan     #here id, name,age are private and pan is public

    def show(self): # public method ; can be callsed outside the class
        print(self.__id)
        print(self.__name)
        print(self.__age)
        print(self.pan)

    def show1(self):
        print(self.__id, self.__name, self.__age)

    def __process(self): #private method ; cannot be called outside the class
        print("hello im in private")


#here  PersonInfo is the class
#__id , __name , __name are  instance varioables
#show()  is instance method and is public
#__process() is instance method and is private

#private cannot be accessed outside the class




myObj = PersonInfo(12000, "murali", 34, "myTestPan")
myObj.show()

