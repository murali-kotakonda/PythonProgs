"""


Ex1:
Req: create obj , set data display

hint:
make instance variables private


"""

class PersonInfo:

    def __init__(self, pId, pName, pAge):
        self.__id = pId
        self.__name = pName
        self.__age = pAge
        # here __id , __name , __name are private [cannot access outside class]

    def show(self):
        print(self.__id,self.__name,self.__age)



p1 = PersonInfo(10000,"shyam",34)
p1.show()



#here  PersonInfo is the class
#__id , __name , __name are  instance varioables
#show() is instance method and is public
#__process() is instance method and is private

#private cannot be accessed outside the class

