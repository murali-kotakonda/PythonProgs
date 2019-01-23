input = "Welcome to python programming"

res = input.startswith("Hi")
print(type(res))
print(res)

#if input.startswith("Hi")
if res:
    print("value begings with Hi")
else:
    print("value doesnt beging with hi")    


res=False

print(input.startswith("Welcome"))


#length of string
size = len(input)
print(size)

#serach string
str1 = "python"
str2="java"
print(input.find("elcome"))

n1 = input.find(str1)

if n1>=0:
    print("string "+str1 +" is available")
else:
        print("string "+str1 +" is not available")

print(input.find(str1))
print(input.find(str2))

str1="hello user"
str2= "bye"
str3 = str1+ str2

print(str3)


# repeater
str1="****************"
print(str1 * 3)



#frequency
str1="hello kumar, welcome to python programming. kumar"
print(str1.count("kumar"))
print(str1.count("welcome"))
print(str1.count("welcome1"))

print(str1.count("kumar", 10))
print(str1.count("kumar", 0,20))


#substrings
print(str1[0])
print(str1[0:3])
print(str1[0:5])
print(str1[:5])


print(str1[-1])
print(str1[-3])
print(str1[5:-3])

str1 ="e1234:kumar:25:hyd"

res= str1.split(":")
print(res[3])

