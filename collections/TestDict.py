myDict ={"3000" : "user3",
         "4000" : "user4",
         "5000" : "user5",
         "1000" : "user1",
         "2000" : "user2",
    }

print(myDict)


#retrive data
print(myDict["1000"])
print(myDict.get("1000"))


#update exsting data
myDict["1000"] = "user100"
print(myDict["1000"])

# add new element'[
myDict.update({"7000":"user7"})
print(myDict)

a= "9000"
b= "user9"
myDict.update({a:b})
print(myDict)

#delete data 
del myDict["5000"]

#get keys
print(myDict.keys())

#get valuez
print(myDict.values())


for k,v in myDict.items():
    print("key = ", k ,"value= ", v)
    
check = "2000" in myDict.keys() 
print(check)   