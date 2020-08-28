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
    
print(chr(120)) # unicode to char
print(ord('x')) # char to unicode



print(format(25, '%'))



print(len(myConditions))

print(type(12))

printList(range(5));

printList(range(2, 5))

printList(range(1, 10, 2))

print(isinstance(12, int))
print(isinstance('hello', int))


