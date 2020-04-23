# Str is commonly data type
# by defualt we have buildin strin operations

name= "hi Eminent It  technologies bye"

# find length of string
size = len(name)
print("length of str==", size)


#upper
name="Hi How Are you"
upStr = name.upper() # creates a new string

lowStr = name.lower() # creates a new string
print(upStr)
print(lowStr)


# string is ending with "bye"
name= "hi Eminent technologies bye"
flag = name.endswith("bye")
if flag:
    print("string ends with bye")
else:
    print("string doesnt end with bye")
    
# string is starts with "bye"
flag = name.startswith("hi")    
if flag:
    print("string begins with hi")
else:
    print("string doesnt begins with hi")
    

# word "tech" is substring of name??????
name= "hi Eminent technologies bye"
s1="tech"
s2 ="hi"
s3="xyz"

charNo = name.find(s1) # retuns int
print(charNo)

charNo = name.find(s3) # retuns int
print(charNo)

charNo = name.find(s3) # retuns int
print(charNo)



# find method returns int
# int value >=0 ===> string is found
# int value ==-1  ===> string is not found

#find :---->>>> check sub string or find the position no
print(name.index("tech"))
# index funtion retunrs posi no: if the string is not found it throws exception
 


# string concatenation
name1 = "bangalore"
name2="india"
name3 = name1 + name2
print(name3)


#repeater
name= "kumar"
name2 = name * 5
print(name2)


# frequency
str ="Hi shyam ! where are you shyam!! im back to work , shyam"
# find no of times the word "shyam" is repetaed in string  from 0 position
countStr = str.count("shyam")
print(countStr)


# find no of times the word "shyam" is repetaed in string strating from 10th position
countStr = str.count("shyam",10)
print(countStr)


# find no of times the word "shyam" is repetaed in string strating from 0th position
#till 15th postion
countStr = str.count("shyam",0,15)
print(countStr)


#split operation data in string seperated by #
inputStr ="kumar#23#2334566#bncpk97404"
data = inputStr.split("#")  # retuns an array
print(data[0])
print(data[1])
print(data[2])
print(data[3])


name="userR"
print(name.isalpha()) # returns true if all chars are alphabets [a-z] [A-Z]
name="1213242"
print(name.isdigit()) # returns true if all chars are digits [0-9]
name="user134131@"
print(name.isalnum()) # returns true if all chars are alphabets + digits[a-z] [A-Z] and [0-9]


name= " shyam !!! kumar!! harsha!! jaya! shyam"
newStr= name.replace("shyam", "shubham")
print(newStr)



# extract substring
str ="hellouser! welcome to python! programmming is fun"
print(str[0])
print(str[0:3])# substring from 0 position to 2nd position
print(str[:4]) # extract 1st n chars

print(str[10:25])# from 10th till 24


print("lasstt")
print(str[-1]) # last but one  n
print(str[-3]) # last but three f

print(str[:-3]) # from 0 position till (size-3) position
print(str[-3:]) # last three chras


#capitalize :-- convert 1st char to capital
# center() :-- centre char
#islower() - is in lower?
#isuuper() - is in upper?
#isnumeric()
#lstrip() ---> trim the white spaces in the begining
#rstrip() ---> trim the white spaces at end
#replace()




# input : sentence   o/p: no of times  a word has been repetaed??
# hi kumar shyma kumar varsa shyam ram kumar

