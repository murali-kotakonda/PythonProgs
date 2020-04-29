class Student:
    def __init__(self, b, s, r):  # this is constr
        self.branch = b
        self.sem = s
        self.rollNum = r

    # here branch , sem,  rollNum are the instance variables
    # b,s,r are the local varibales.
    def show(self):
        print("show funtn called")


s1 = Student("CSE", 2, 2000)
print(s1.branch, s1.sem, s1.rollNum)
s1.show()

s2 = Student("ECE", 3, 3000)
print(s2.branch, s2.sem, s2.rollNum)
s2.show()





class Student:
    def __init__(self,b,s,r):
        self.branch=b
        self.sem=s
        self.rollNum=r

    def show(self):
            print(self.branch)
            print(self.sem)
            print(self.rollNum)



#create obj with data
p=Student("CSE",2,13131)

p1=Student("ECE",3,1212)

p.show()
p1.show()