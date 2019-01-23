myList = [12, 'krishna', 1414.14144]


print(type(myList))

#get data 
print(myList[0])
print(myList[1])
print(myList[2])

print("#######show using for loop######")
# print data one by one using iterator
for data in myList:
    print(data)
    
#update element
print("#######show after update######")
myList[0] = 'hi'
print(myList[0])    


#add new element
print("#######add new element######")
myList.append("hyderabad")
print(myList)

#add new element at any position
print("#######add new element at position######")
myList.insert(0, 'welcome')
print(myList)

#delete data
print("#######delete data ######")
del myList[0]
myList.remove(myList[0])
print(myList)

# remove last element
print("#######after pop ######")
myList.pop()
print(myList)


# search by content
print("#######search by content ######")

res = 'krishna' in myList
if res:
    print('krishna found')
else: 
    print('not found')
    
# remove by content
print("#######remove by content ######")
myList.remove('krishna')
print(myList)


# merge lists
print("#######merge #####")
myList2 = ['sap', 'java' ,'hana','sap']

mylist3= myList + myList2
print(mylist3)

myList.extend(myList2)
print(myList)
