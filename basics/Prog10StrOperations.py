myStr ="Hi user, how are you, where are, you "


toUp = myStr.upper();
print(toUp);
print(myStr)

print(myStr.endswith("BYE"))

if not(myStr.endswith("bye")):
    myStr =  myStr +" bye."
    
print(myStr)

print(myStr.find("user"))
print(myStr.find("KRISHNA"))

print(myStr.index("user"))
#print(myStr.index("krish"))

print(len(myStr))

arr = myStr.split(",")
print(arr[0])
print(arr[1])


str ="Hello"
print(str * 2)



print(myStr.count("are"))
print(myStr.count("you"))
print(myStr.count("Hi"))
print(myStr.count("Krish"))



print(myStr.count("are",14))

print(myStr.count("are",13, 20))




print(myStr[0])
print(myStr[0:2])
print(myStr[0:4])
print(myStr[0:5])


print(myStr[-1])
print(myStr[-2])
print(myStr[5:-2])

