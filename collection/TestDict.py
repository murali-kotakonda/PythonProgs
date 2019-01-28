mySet = {"user1","sap" ,"hana","java","hana","sap", 1,"SAP",20,20.01}

print(mySet)

#Add new element in set
print("*************add operation***********")
mySet.add("java")
mySet.add("sap")
mySet.add("angular")
print(mySet)

#search by content
print("*************search by content***********")
res = 'sap' in mySet
print(res)


mySet2 = {'jquery','selenium','sap','java'}

print("set2==",mySet2)
print("*************mySet-mySet2***********")
set3 = mySet-mySet2
print(set3)


print("*************mySet2-mySet***********")
set3 = mySet2-mySet
print(set3)


print("*************mySet|mySet2***********")
set3 = mySet|mySet2
print(set3)



print("*************mySet&mySet2***********")
set3 = mySet&mySet2
print(set3)



print("*************mySet^mySet2***********")
set3 = mySet^mySet2
print(set3)

set3.remove('angular')
print(set3)

list= ['user1','user4','user10','user1','user6','user1']

newSet = set(list)
print(list)
print(newSet)