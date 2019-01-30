myList = [10,50,90,55,60,5]

print(type(myList))

#print all
print(myList)


myList = [12, "krishna", 12.1331 , 39]

print(myList)


#search by index
print(myList[2])   # get element by posistion 3
print(myList[0])   # get element by posistion 1


# add new element
myList.append("user1")
print(myList );

# add element at 2nd position
myList.insert(1,"user2")
print(myList );

# update element at position 4
myList[3] = "data1"
print(myList );

#concat operations
# newList = myList + ['sap','hana']
# print(newList);
# print(myList );


#merge two lists
# myList.extend(['sap','hana'])
# print(myList );

