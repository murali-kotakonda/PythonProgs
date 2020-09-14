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

"""
def printList(list):
    print("-------------------")
    for i in list:
        print(i)


# any () -> takes multple conditions as input and returns trur if any condition is true
myConditions = [True, True, True, True]
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

#check for data type
x= 12
print(isinstance(x, int))

x= 'hello'
print(isinstance('hello', str))


