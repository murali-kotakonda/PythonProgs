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

    def __myprivate(self): #private method ; cannot be called outside the class
        print("hello im in private")

myObj = PersonInfo(12000, "murali", 34, "myTestPan")
myObj.show()

