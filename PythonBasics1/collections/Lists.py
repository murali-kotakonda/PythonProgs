#Create a list with data
myList = [12, 'krishna', 4587.432 ]


# stores data of diff data types
print(type(myList))
print(myList)

#find length : use len() function
print("length of list = ",len(myList))

# search by position
print("************************** search by position ************************************")
print(myList[0])
print(myList[1])
print(myList[2])


print("************************** Add new element ************************************")
# update the list or add element to list
# add new element to list
# use append() funtion
myList.append("bangalore")
print(myList)
# myList[5] ="bangalore" # not supported for insert
print(myList)

print("************************** Add in between ************************************")
# insert in between, use insert() funtion mention position num and new element
myList.insert(1, "myNewPancard")
print(myList)


print("************************** update  existing element ************************************")
# update an existing element
myList[2] = 60000.78
print(myList)

print("************************** search by content ************************************")
# search by content : use 'in' keyword
print('bangalore' in myList)
print('delhi' in myList)

print("**************************  find position of element ************************************")
# find position of element ,   if element not found throws exception
print(myList.index("krishna"))
# print(myList.index("krishna1"))

print("************************** remove element by content ************************************")
# remove by element value
myList.remove("myNewPancard")
# myList.remove("myNewPancardazffsf") # throws exception if not found
print(myList)

print("************************** remove by position ************************************")
# remove by position
del myList[1]
#myList.remove(myList[0])
print(myList)


cities = ['bangalore', 'chennai', 'mumbai', 'hyd']
city = input("enter city")

if (city in cities):
    print("service provied")
else:
    print("service not provided")



print("*********iterate and print ************")
for data in myList:
    print(data)






# deletes the last element
myList.pop()
print(myList)

myList.append("user1")
myList.append("user2")
myList.append("user3")
myList.append("user4")
myList.append("user5")
myList.append("user6")
myList.append("user8")

# iterate all elements
print("****print all*****")
for i in range(len(myList)):
    print(myList[i])

print("****print all*****")
for data in myList:
    print(data)

# concatenate
myList2 = [1, 2, 3, 4, 5, 6]
myList3 = myList + myList2
print(myList)
print(myList2)
print(myList3)


# delete all elements : empty list
myList.clear()


# min,max and sum functions,xiunt
intList = [1, 2, 3, 535, 35, 35, 5, 1]
print(max(intList))
print(min(intList))
print(sum(intList))
print(intList.count(1))  # frequency


"""

# slicing
print("printing 0 to 2", myList[-1])
print("printing 0 to 2", myList[0:2])

# repeat
print("repeat--->>", myList * 2)

# empty list
myList.clear()

# APPEND 2ND LIST TO 1ST LIST
myList = myList + myList2
myList.extend(myList2)
print(myList)

# Read data from db and return to front end
myList = [('name', 'id', 'age'), ('murali', 234, 25), ('vamsi', 28009, 29), ('saranya', 5644, 29)]

for k in myList:
    print(k)



def removeDuplicate(li):
    newli = []
    seen = set()
    for item in li:
        if item not in seen:
            seen.add(item)
            newli.append(item)

    return newli


li = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]
print(removeDuplicate(li))

# convert list to bytes
b = bytes(myList)
# b1[1] =32 Not allowed
print(type(b))

# convert list to bytes array
b1 = bytearray(myList)
b1[1] = 32  # allowed
print(type(b1))

"""

"""
With a given list [12,24,35,24,88,120,155,88,120,155], write a program to print this list after removing all duplicate values with original order reserved.

Hints:
Use set() to store a number of values without duplicate.

Solution:
"""








