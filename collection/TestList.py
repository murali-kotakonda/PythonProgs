def showList(inputList):
    for data in inputList:
        print("item = ",data)



myList = [12,"kumar",13131.1313,'sap','hana','hadoop','jquery']

print(type(myList))

#print list elements
print(myList)

#iterate all
showList(myList)    
# get 1st element
print(myList[0])

#chnage data
myList[0] = 90
print(myList[0])

# add new element
myList.append("bangalore")
showList(myList)  

#add "java" at 1st position
myList.insert(0,"java" )
print(myList[0])
print(myList[1])
print(myList)

#delete

del myList[0]
print(myList)

myList.remove(myList[0])
print(myList)

myList.pop()
print(myList)

#find length
print(len(myList))


#search by content
res = "hana" in myList
print(res)

res = "xyz" in myList
print(res)


#merge of two lists
mylist2 = ["----","hana","java","hadoop","j2ee"]
#myList.extend(mylist2)
myList3 = myList + mylist2
print(myList3)


