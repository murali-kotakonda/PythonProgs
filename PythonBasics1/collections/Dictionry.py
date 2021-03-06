"""
 list/tuple/set every entry contains one data

in case of dictionary every entry contains [key] and [value]
  - key can be any datatype
  - value can be any data type
  - keys are unique
  - any operation u need perform using the key

-List, Tuple are index based operations.
 insert/update/delete/read based on position.

- Dict is a content based operation.
 insert/update/delete/read based on content.

search by content is fast
"""

myData = {
    "name":"murali",
    "age" : 25,
    "id" : 3456
}
"""
  there are three entries
  name , age  id are the keys.
  murali , 25 , 3456 are the values 
   
  key and value are seperated by :
 
  very entry is seperated by comma
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


print("*********add duplicate key ******")
myData.update({"sal" : 90000})
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


print("*****************remove based on key[  name ]****************************")
del myData["name"] # this dletes the key and value
print(myData)

# iterate the dictionary
print("************************printing entire dictinary******************************")
for k,v in myData.items():
    print("key = ", k , "value = ", v)


# delete all entries
myData.clear()