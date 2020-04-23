def add(n1, n2):
    print("from global ", n1 + n2)


class Cal:

    def add(self,n1,n2):
        print(n1+n2)

    def sub(self,n1,n2):
        print(n1 - n2)

    def mul(self,n1,n2):
        print(n1 * n2)

    def div(self,n1,n2):
        print(n1 / n2)


num1 = int(input("enter n1"))
num2 = int(input("enter n2"))

c1 = Cal()
c1.add(num1,num2)
c1.sub(num1,num2)
c1.mul(num1,num2)
c1.div(num1,num2)


num1 = int(input("enter n1"))
num2 = int(input("enter n2"))

c2 = Cal()
c2.add(num1,num2)
c2.sub(num1,num2)
c2.mul(num1,num2)
c2.div(num1,num2)

add(num1,num2)