# key - String , value --> List
myEmpData = {'names': ['murali', 'vamsi', 'saranya'],
             'ids': [100, 101, 102],
             'ages': [20, 21, 22]}

# iterate emp data
print("printing entire emp info")
for k, v in myEmpData.items():
    print("key =", k)
    print("values are =")
    for i in range(len(v)):
        print(v[i])

print(myData['name'])

# delete the entry in the dictiony
del myData['name']  # both key and value are delyte
myData.pop("sal")

# print(myData['name']) # key not found , run time exception.

# copy content fro one dict to another dict
myNewDic = myData.copy()
print(myNewDic)
