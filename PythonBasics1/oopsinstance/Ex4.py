


class Person:

    def __init__(self,pId,pName,pAge):
        self.id= pId
        self.age= pAge
        self.name= pName

    def show(self):
        print(self.id)
        print(self.name)
        print(self.age)

#CLASS: Person
#instane variables : id,name,age
#pId,pName,pAge local variables

#show() is the instance function

# create the obj ,set data and print the data

print("*********** Show p1 **************")
p = Person(2000,"user1" , 34)
p.show()
# if show() is called using 'p' , then show() print the data for 'p'

print("*********** Show p2 **************")
p1 = Person(2001,"user2" , 35)
p1.show()
# if show() is called using 'p1' , then show() print the data for 'p1'

print("*********** Show p3 **************")
p2 = Person(2002,"user3" , 35)
p2.show()
# if show() is called using 'p2' , then show() print the data for 'p2'