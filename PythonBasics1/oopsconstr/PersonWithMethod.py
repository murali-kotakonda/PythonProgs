def myFuntn():
    print("welcome to my funtn")

class Person:

    def __init__(self, pId, pName, pAge):
        self.id = pId
        self.name = pName
        self.age = pAge

    def showMyData(self):
        print(self.id,self.name,self.age)


#create obj with data
p=Person(2000,"USER1",45)

p1=Person("user1",2000,47)
p1.name="user5" #change only the name

p.showMyData()
p1.showMyData()
 