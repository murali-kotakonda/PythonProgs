class Person:
    def __init__(self,pId,pName,pAge):
        self.id=pId
        self.name=pName
        self.age=pAge

    def show(self):
            print(self.id)
            print(self.name)
            print(self.age)

    def __str__(self):
        '''return "id =" + str(self.__id) +", nanme="+self.__name'''
        return "id={}, and name={}, age= {} , pan= {}".format(self.id, self.name,self.age)

#create obj with data
p=Person(2000,"USER1",45)

p1=Person(2001,"user2",47)
p1.name="user5" #change only the name

print(p.id)
print(p.name)
print(p.age)

print(p1.id)
print(p1.name)
print(p1.age)