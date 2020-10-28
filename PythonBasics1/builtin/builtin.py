"""
print()
input()
range()
int()
float()
complex()
str()
tuple()
list()
set()
dict()
len()
type()
open()
"""


def printList(list):
    print("-------------------")
    for i in list:
        print(i)


# any () -> takes multiple conditions as input and returns true if any condition is true
myConditions = [True, True, True, True]
myConditions = [5>7, 8<9 ,6>5, 1==1]
if(any(myConditions)):
    print("procced")
else:
    print("stop")

# all () -> takes multple conditions as input and returns true if all condition is true
if(all(myConditions)):
    print("procced")
else:
    print("stop")

# unicode to char
print(chr(120))


# char to unicode
print(ord('x'))



print(format(25, '%'))



print(len(myConditions))

print(type(12))

printList(range(5));

printList(range(2, 5))

printList(range(1, 10, 2))

#how to identify datatype : type()
#how to compare data type: isinstance()

#check for data type
x= 12
print(isinstance(x, int))

x= 'hello'
print(isinstance('hello', str))


