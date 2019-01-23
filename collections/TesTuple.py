myList = (12, 'krishna', 1414.14144)


print(type(myList))

#get data 
print(myList[0])
print(myList[1])
print(myList[2])

print("#######show using for loop######")
# print data one by one using iterator
for data in myList:
    print(data)
    

# search by content
print("#######search by content ######")

res = 'krishna' in myList
if res:
    print('krishna found')
else: 
    print('not found')
     

# merge lists
print("#######merge #####")
myList2 = ('sap', 'java' ,'hana','sap')

mylist3= myList + myList2
print(mylist3)

