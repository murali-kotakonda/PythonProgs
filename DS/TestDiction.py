myMap = {
    "1000":"user1",
    "1001":"user2",
    "1003":"user3",
    "1004":"user4",
    7890:14555,
    67576:"shyam"
    }

print(myMap)

#serach by key
print(myMap["1000"])
print(myMap.get("1000"))

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
    
#remove based on key
del myMap["1000"]
print(myMap)
    

    











