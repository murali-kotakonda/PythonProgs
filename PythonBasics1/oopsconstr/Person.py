
#create a class
#provide the constr

#create obj using constr
#print obj data


class Person:

    # constructr logic start
    def __init__(self, pId, pName, pAge):
        print("constr called")
        self.id = pId
        self.name = pName
        self.age = pAge
    # constructr logic end

    def show(self):
            print(self.id)
            print(self.name)
            print(self.age)


# Create object

p1 = Person(2000, "kumar", 34)  # obj is created , internally calls __init__

p2 = Person(2001, "ram", 38)  # obj is created , internally calls __init__

p3 = Person(2003, "raj", 39)  # obj is created , internally calls __init__


print(p1.id,p1.name,p1.age)
print(p2.id,p2.name,p2.age)
print(p3.id,p3.name,p3.age)



#create obj with data
p=Person(2000,"USER1",45) # obj is created , internally calls __init__
p1=Person(2001,"user2",47)  #  obj is created , internally calls __init__

p.show()
p1.show()

p1.name="user5" #change only the name


print(p.id)
print(p.name)
print(p.age)

print(p1.id)
print(p1.name)
print(p1.age)