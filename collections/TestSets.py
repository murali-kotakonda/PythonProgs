mySet = {'sap','hana','java','hadoop','jquery','selenium','sap','java','hana'}

print(mySet)


# add new element in set
print("**************add new element************")
mySet.add("bigdata")
mySet.add("sap")
print(mySet)

#search by content
print("**************search by content************")
result = 'sap' in mySet
print(result)

#delete elemnt (remove nby content)
print("**************delete element************")
mySet.remove('sap')
print(mySet)

mySet2 ={"hana","java","python","oracle"}
print(mySet2)

print("**************mySet1- mySet2************")
res = mySet - mySet2;
print(res)

print("**************mySet1| mySet2************")
res = mySet | mySet2;
print(res)


print("**************mySet1& mySet2************")
res = mySet & mySet2;
print(res)


print("**************mySet1^mySet2************")
res = mySet ^ mySet2;
print(res)


# convert list to set
myList = [1,2,3,4,1,4,1,7,8,9,1,3]
myset7 = set(myList)
print(myList)
print(myset7)



