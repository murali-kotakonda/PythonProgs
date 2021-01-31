list = [10, 20, 30,40]

try:
    print(list[0])
    print(list[7]) # trying to access 8th element but list has 3 elements
except IndexError as ex:
    print("exception occured , please use the correct index ")
else:
    print("No exception")

print(list[2])
print("Bye")


#in this case python creates IndexError


