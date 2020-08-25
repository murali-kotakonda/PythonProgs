"read file"

f3 = open("user.txt", "r")
print(f3.read()) #print all


f3.seek(0)
#iteratively print every line
for line in f3:
    print( line)


f3.seek(0)
print(f3.readlines())  # fetch all lines in the file

print("read line by line")
f3.seek(0)
print(f3.readline()) #print the entire  1st line
print(f3.readline()) #print the entire  2nd line
print(f3.readline())


print("read by no of chars")
f3.seek(0)
print(f3.read(5))
print(f3.read(5))

print("read by line and char ")
f3.seek(0)
print(f3.readline(3))
print(f3.readline(4))
print(f3.readline(10))


"""read specified no of characters
print(f3.read(5)) - print 1st 5 chars
print(f3.readline(3)) --> read 3rd line 

 
"""



f3.close()


