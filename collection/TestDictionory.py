myDict = {"1000":"user1",
          "2000":"user2",
          "3000":"user3",
          "4000":"user4",
          "5000":"user5"}


print(myDict)

#get by key
print("******get by key*****")
print(myDict.get("5000"))
print(myDict["5000"])


print("******update by key*****")
myDict.update({"5000":"user6"})
print(myDict["5000"])

myDict["5000"] = "user7"
print(myDict["5000"])


#add new key +value
myDict.update({"9000":"user9"})
print(myDict)

#delete operation
del myDict["9000"]
print(myDict)

#check if key exists
res = "9000" in myDict.keys()
print(res)
res = "2000" in myDict.keys()
print(res)


#iterate all
for k,v in myDict.items():
    print("key = ",k , "value= ",v)
