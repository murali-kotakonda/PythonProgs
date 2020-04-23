# declaration of a set
#will not allow duplicates
# item
myset = {1, 45, 3,4,1, 1, 23, 0, -1 }
print(myset)

# creating a set using a constructor
mySet6 = set()
print(mySet6)

myset2 = {'sap', 'java', 'hana', 'sap', 'hadoop', 'angularjs', 'java'}
print(myset2)

myset3 = {1, 'murali', 23, 'murali', 23, 1}
print(myset3)


# to add entry into the set
myset3.add('mythri')
print(myset3)

# serach by content
print('murali' in myset3)

# length
print("size of set===========  ", len(myset3))

# iterate the  set
for data in myset3:
    print("element= ", data)

# delete from set
print("user2" in myset3)
myset3.remove("user2")
print("user2" in myset3)
print(len(myset3))

myset4 = {1, 'murali', 23}
myset5 = {'murali', 'banglalore', 'India'}
# Plus operation is not applied for sets
# Minus operation for sets :---- elements prest in set1 but not in set2
print(myset4 - myset5)  # print wat is avilable in myset4 but not in myset5

print(myset5 - myset4)

# Union Opearation , merging both sets by avoiding duplicates
print(myset4 | myset5)

# Common in both the sets
print(myset4 & myset5)

# symmetrci diff
print("see")  # MERGE BOTH AND REMOVE COMMONS
print(myset4 ^ myset5)

# convert list to set
myList = [1, 2, 3, 4, 1, 4, 1, 7, 8, 9, 1, 3]
myset7 = set(myList)
print(myList)
print(myset7)

# convert a tuple to set
myTupl = (1, 2, 3, 4, 1, 4, 1, 7, 8, 9, 1, 3)
myset8 = set(myTupl)
print(myTupl)
print(myset8)

# converst set to frozewn set ; frozen will no any update/remove operations; used only for read operations
f = frozenset(myset)
print(type(f))
