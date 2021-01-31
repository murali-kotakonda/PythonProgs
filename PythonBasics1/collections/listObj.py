"""

one person has multiple objects:


"""

class Person:
    def __init__(self,id,name,age):
        self.id=id
        self.name=name
        self.age=age


list=[]

#add person objs to list
p1 = Person(2000,"user1",23)

p2 = Person(2001,"user2",24)

p3 = Person(2002,"user3",25)

#add objs inside the list
list.append(p1)
list.append(p2)
list.append(p3)

#print objs using list
for p in list:
    print(p.id)
    print(p.name)
    print(p.age)

"""
#assignment:

Take size as input [how many persons??]
Take id,name,age for size no of times ,
finally print all the persons info

hint:use list

"""