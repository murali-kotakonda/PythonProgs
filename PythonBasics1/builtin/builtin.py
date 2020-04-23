
def printList(list):
    print("-------------------")
    for i in list:
        print(i)


myConditions = [True, True, True, True]
if(any(myConditions)):
    print("procced")
else:
    print("stop")
    
if(all(myConditions)):
    print("procced")
else:
    print("stop")
    
print(chr(120))
print(ord('x'))



print(format(25, '%'))



print(len(myConditions))

print(type(12))

printList(range(5));

printList(range(2, 5))

printList(range(1, 10, 2))

print(isinstance(12, int))
print(isinstance('hello', int))


input()
type()
print()
range()