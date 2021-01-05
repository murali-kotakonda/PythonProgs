class Data:
    def __init__(self,n1,n2):
        self.n1=n1
        self.n2=n2

    def __add__(self, other):
        num1= self.n1 + other.n1
        num2 = self.n2 + other.n2
        d = Data(num1,num2)
        return d

    def __sub__(self, other):
        num1 = self.n1 - other.n1
        num2 = self.n2 - other.n2
        d = Data(num1, num2)
        return d

    def __str__(self):
        return "{0} , {1}".format(self.n1,self.n2)

d1= Data(40,20)

d2= Data(5,6)

d3 = d1 + d2 # internally calls __add__
print(d3.n1)
print(d3.n2)


d3 = d1 - d2 # internally calls __sub__
print(d3.n1)
print(d3.n2)



"""
      
# + , - , * , / --->
if we need to apply the opeartors on the objects; then developer has to write a method inside the class for every operator.
  

d4 = d1 + d2 + d3
print(d4.n1)
print(d4.n2)
"""

'''     
p1 and p2 are objects.

Operation          how to operate                method to override
addition            p1 + p2                        __add__
Subtraction         p1 - p2                        __sub__
Multiplication      p1 * p2                        __mul__
Power               p1 ** p2                       __pow__
Division            p1 / p2                        __truediv__
Floor Division      p1 // p2                       __floordiv__
Remainder (modulo)  p1 % p2                        __mod__
Bitwise Left Shift  p1 << p2                       __lshift__
Bitwise Right Shift p1 >> p2                       __rshift__
Bitwise AND         p1 & p2                        __and__
Bitwise OR          p1 | p2                        __or__
Bitwise XOR         p1 ^ p2                        __xor__
Bitwise NOT        ~p1                             __invert__() 

Less than                  p1 < p2                        __lt__
Less than or equal to      p1 <= p2                       __le__
Equal to                   p1 == p2                        __eq__ 
Not equal to               p1 != p2                       __ne__
Greater than               p1 > p2                        __gt__
Greater than or equal to   p1 >= p2                       __ge__
'''
