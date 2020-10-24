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


