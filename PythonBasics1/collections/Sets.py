# declaration of a set
# will not allow duplicates
# search by content is fast
# insertion order is not maintained.
# item

#set for nums
myset = {1, 45, 3,4,1, 1, 23, 0, -1 }
print(myset)

# creating a set using a constructor
mySet6 = set()
print(mySet6)


#set for strings
myset2 = {'sap', 'java', 'hana', 'sap', 'hadoop', 'angularjs', 'java'}
print(myset2)



#set with data of multiple data types
myset3 = {1, 'kumar', 23, 'kumar', 23, 1}
print(myset3)



# to add entry into the set
myset3.add("mythri")
myset3.add("mythri")
myset3.add("mythri")
print(myset3)


#search by content use 'in'
print('kumar' in myset3)
print('ram' in myset3)

#length
print(len(myset3))

print("--------------iterate all-------------------------")
#iterate all elements
for data in myset3:
    print(data)

print("------------delete kumar----------------")
#delete by content
myset3.remove("kumar")
print(myset3)
print(len(myset3))



myset4 = {1, 'raj', 23}
myset5 = {'raj', 'banglalore', 'India'}

print("***********minus operation***************")
#perform minus operation on sets [ what is present in set1 but not in set2]
res = myset4-  myset5
print(res)

res = myset5-  myset4
print(res)

# Union Opearation , merging both sets by avoiding duplicates, + opeartion is not applicable for sets
print("*****************union of sets*********************************")
res = myset4 | myset5
print(res)

# Common in both the sets
print("*************common in sets********************8")
res = myset4 & myset5
print(res)

# symmetric diff  # MERGE BOTH AND REMOVE COMMONS
print("****************symmetric diff******************")
res = myset4 ^ myset5
print(res)

#how to convert list or tuple to a set
#solution : use set() function.


# convert list to set
myList = [1, 2, 3, 4, 1, 4, 1, 7, 8, 9, 1, 3]
resSet = set(myList)
print("list = ",myList)
print("set = ",resSet)

# convert a tuple to set
myTupl = (1, 2, 3, 4, 1, 4, 1, 7, 8, 9, 1, 3)
resSet = set(myTupl)
print("tuple = ",myTupl)
print("set = ",resSet)









"""

# converst set to frozewn set ;
# frozen will no any update/remove operations; used only for read operations
f = frozenset(myset)
print(type(f))

"""