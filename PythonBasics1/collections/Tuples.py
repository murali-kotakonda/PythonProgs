# declare list
myList = (12,'krishna', 4587.432) # stores data of diff data types

print(type(myList))
print(myList)

#search operations
print(myList[0])  # search  by index
print(myList[2])  # search  by index

#slicing
print("printing 0 to 2",myList[-1])
print("printing 0 to 2",myList[0:2])

#repeat
print("repeat--->>",myList*2)

#concat
print(myList + ('sap',123))


#get position of the element in the list , if element not found throws exception
print(myList.index(12))


#find length
print(len(myList))

# search by content
print('bangalore' in myList)

#iterate all elements
for i in range(len(myList)):
    print(myList[i])
     
#slicing
print(myList[0:2]) # start from position 0 and display two elements
print(myList[-1]) #  prints the last element


#trepeat
print(myList*2)


#concat
myTuple1 =  ('1','2')
newTuple = myList + myTuple1;
print(newTuple)
