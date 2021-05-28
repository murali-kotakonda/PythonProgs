"""
write a instance function to display the obj data

"""

class Person:
    id= None
    age= None
    name= None

    def printObjData(self):
        print(self.id)
        print(self.name)
        print(self.age)


p1 = Person() # new object is created


#set data
p1.id = 9000
p1.name="user1"
p1.age=45


p2 = Person() # new object is created


#set data
p2.id = 9001
p2.name="user2"
p2.age=46


print("****************Print p1 ********************")
p1.printObjData()
#if printObjData() function is called using p1 then self = p1
#if printObjData function is called using p1 then logic of printObjData() function is applied on p1's data

print("****************Print p2 ********************")
p2.printObjData() #if printObjData() function is called using p2 then self = p2
#if printObjData function is called using p2 then logic of printObjData() function is applied on p2's data
