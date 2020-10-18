# dictionay , every entry contains [key] and [value]
# list/tuple/set every entry contains one data
# key can be any datatype
# value can be any data type


"""


 # contain or hold two elaments == key and value
# any operation u need perform using the key
# key , value ----> hashmap
# keys are unique



#Dictionary:
#in dict every entry has two elements
1.KEY   -> ANY DATATYPE
2.VALUE  -> ANY DATA TYPE

Tuple/List/Set one entry contains only one element


List, Tuple are index based operations.
insert/update/delete/read based on position.

Dict is a content based operation.
insert/update/delete/read based on content.


"""

myData = {
    "name":"murali",
    "age" : 25,
    "id" : 3456
}
"""
  there are three entries
  name , age  id are the keys 
 key and value are seperated by :
  every entry is seperated by comma
Keys are unique

"""
print(myData)
print(type(myData))

print("********get based on key*********")
#retrieve based on key
print(myData["name"])
print(myData["age"])
print(myData["id"])

#add new entry to dictionary: use update
print("*********add new entry sal*******")
myData.update({"sal" : 40000})
print(myData)


#update existing entry
#approach1
print("*********update entry sal*******")
myData.update({"sal" : 50000})
print(myData)

#approach2
print("*********update entry name*******")
myData["name"] ="raj kumar"
print(myData)

# length
print("********Lenghth = ***********")
print(len(myData))

# get the keys - use keys() function
print("******** get only keys  = ***********")
myKeys = myData.keys();
print(myKeys)


# get the values - use values() function
print("******** get only values  = ***********")
myvalues = myData.values()
print(myvalues)

# iterate the dictionary
print("************************printing entire dictinary******************************")
for k,v in myData.items():
    print("key = ", k , "value = ", v)


#check if the key exists : use in operation along with keys() function
# check if the key exists
if 'name' in myData.keys():
    print('name key  found')
else:
    print('name key not found')

if 'deptId' in myData.keys():
    print('deptId key found')
else:
    print('deptId key not found')

print("*************remove based on key[  name ]**********")
del myData["name"] # this dletes the key and value
print(myData)

