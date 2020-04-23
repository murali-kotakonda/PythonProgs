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