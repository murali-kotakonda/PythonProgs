

mySet = {"sap","hana","java","sap","python","dotnet","java"}
print(mySet)


# add element into set
mySet.add("angularjs")
print(mySet)

#serach by content
print("java" in mySet)
mySet2 = {"sap","hana","jquery"}
print(mySet - mySet2)

#merge two sets - union & avoid duplicates
print(mySet | mySet2)

#get the common between two sets
print(mySet & mySet2)

#symmetric : print everything except the common
print(mySet ^ mySet2)

myList = [12, 'krishna', 4587.432,'krishna',12]
mySet3 = set(myList)
print(mySet3) 

print(len(mySet))



