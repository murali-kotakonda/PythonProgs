"read file"

f3 = open("user.txt","r")

print(f3.readline(10))
"""read specified no of characters
print(f3.read()) - print all
print(f3.read(5)) - print 1st 5 chars
print(f3.readline()) - print the entire line
print(f3.readline(10)) -- print specified no of char in the line
print(f3.readlines())  --> fetch all lines in the file
iteratively pint every line
for line in f3:
    print(line)
"""

#To read a list of lines use:
print(f3.readlines())


f3.close()


