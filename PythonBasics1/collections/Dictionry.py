# dictionay , every entry contains [key] and [value]
# list/tuple/set every entry contains one data
# key can be any datatype
# value can be any data type

# key should be unique
"""
#words :
# how many times a word has been repeated
#5 ,   ---> sap , hana , sap , hana, java
# sap--> 2 , hana--> 2 , java --1


# Requirement : words as input
# find word count
# Collection ----> person objs . p1,p2,p3,p4,p5,p6.
#  find p6 ----> set

# Dictionary == Hashmap 
# contain or hold two elaments == key and value
# any operation u need perform using the key
# key , value ----> hashmap
# keys are unique


Deptid, Empid
100 , 500
101 , 800
105, 64544
100 , 800
200 , 765
101, 8754
100 , 790
200 , 2333



o/p:
100     ---> 500, 790, 800
101    ----> 810,8754
105  ---> 64544 
200   ---> 2333, 765

#Dictionary:
#in dict every entry has two elements
1.KEY   -> ANY DATATYPE
2.VALUE  -> ANY DATA TYPE


List, Tuple are index based operations.
insert/update/delete/read based on position.

Dict is a content based operation.
insert/update/delete/read based on content.

Tuple/List/Set one entry contains only one element

"""

myData = {
    "name":"murali",
    "age" : 25,
    "id" : 3456
}
"""
# there are three entries
# name , age  id are the keys 
#key and value are seperated by :
# every entry is seperated by comma
Keys are unique

"""
print(type(myData))
 # print content
print(myData)

# retrive based on key
print(myData["name"])
print(myData["age"])
print(myData.get("age"))

# add one more entry to dictionay
myData.update({"sal":12344.777})
print(myData)


#add duplicate key
print("add duplicate key")
#update existing entry
myData["name"] = "raj kumar"
myData.update({"name":"shyam"})
print(myData)

# length 
print(len(myData))

# get the keys
myKeys = myData.keys();
print(type(myKeys))


# get the values
myvalues = myData.values()
print(myvalues)

# iterate the dictionary
print("printing entire dictinary")
for k, v in myData.items():
        print(k , v)


#check if the key exists
if 'name' in myData.keys():
    print('key  found')
else: 
    print('key not found')
    
if 'salary' in myData.keys():
    print('key found')
else: 
    print('key not found')

# remove based on key
del myData["name"]
print(myData)



############################################
myMap = {
    "1000":"user1",
    "1001":"user2",
    "1003":"user3",
    "1004":"user4",
    7890:14555,
    67576:"shyam"
    }

print(myMap)


print(myMap.get(67576))

#add new key + value
myMap.update({"1005":"user5"})
print(myMap)

# add same key with diff value
myMap.update({"1000":"user500"})
print(myMap)


#update the existing key, value
myMap["1000"] = "USER600"
print(myMap)


#GET ONLY KEYS
print(myMap.keys())

#GET ONLY values
print(myMap.values())

# traverse the entire dict
for k,v in myMap.items():
    print(k)
    print(v)


    