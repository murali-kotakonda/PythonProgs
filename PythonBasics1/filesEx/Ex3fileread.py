"read file"
"""
#Read operation , mode - r
read()   #returns a string 
readlines()#returns a list  , every line is a element in the list
readline() # read a single line
read(<num>)
readline(<num>)
ex:
f3.read(5) - print 1st 5 chars
f3.readline(3) --> read 3rd line 
"""
print("****************read****************")
f3 = open("user.txt", "r")
x= f3.read()

print(type(x), x) #print all


f3.seek(0)
#iteratively print every line
print("****************read iteratively****************")
f3 = open("user.txt", "r")
for line in f3:
    print( line)


f3.seek(0)
print("****************readlines****************")
f3 = open("user.txt", "r")
x= f3.readlines()
print(type(x), x) #print all
print(f3.readlines())  # fetch all lines in the file


print("****************read line by line****************")
f3 = open("user.txt", "r")
print(f3.readline()) #print the entire  1st line
print(f3.readline()) #print the entire  2nd line
print(f3.readline())

print("read by line and char ")
f3 = open("user.txt", "r")
print(f3.readline(3))
print(f3.readline(4))
print(f3.readline(10))


print("****************read by no of chars****************")
f3 = open("user.txt", "r")
print(f3.read(5))
print(f3.read(5))




"""read specified no of characters
print(f3.read(5)) - print 1st 5 chars
print(f3.readline(3)) --> read 3rd line 

 
"""



f3.close()


