def add(n1, n2):
    print("from global ", n1 + n2)


"""
Requirement:

take two numbers as input and perform
add()
sub()
mul()
div()



#Approach1:
There are no instance variables
1.take 2 nums as input
2.create object
3.call functions using the object by passing the input


"""

class Cal:

    def add(self,n1,n2):
        print(n1+n2)

    def sub(self,n1,n2):
        print(n1 - n2)

    def mul(self,n1,n2):
        print(n1 * n2)

    def div(self,n1,n2):
        print(n1 / n2)

"""
1.take 2 nums as input
2.create object
3.call functions using the object

"""


#take the input
num1 = int(input("enter n1"))
num2 = int(input("enter n2"))


#create object
c1 = Cal()

#call the functions
c1.add(num1,num2)
c1.sub(num1,num2)
c1.mul(num1,num2)
c1.div(num1,num2)



#take the input
num3 = int(input("enter n3"))
num4 = int(input("enter n4"))


#create object
c2 = Cal()

#call the functions
c2.add(num3,num4)
c2.sub(num3,num4)
c2.mul(num3,num4)
c2.div(num3,num4)





