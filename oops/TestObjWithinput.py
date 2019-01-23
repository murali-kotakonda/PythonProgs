from oops.PersonData import Person

id = input("enter id");
name = input("enter name");
age = input("enter age");

p1= Person(id,name,age)
# print(p1.id)
# print(p1.name)
# print(p1.age)
p1.show()

id = input("enter id");
name = input("enter name");
age = input("enter age");


p2= Person(id,name,age)
# print(p2.id)
# print(p2.name)
# print(p2.age)
p2.show()

p2.id=3000
