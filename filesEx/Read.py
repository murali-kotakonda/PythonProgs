f = open("test.txt","r")

#print(f.read())

#print(f.read(5))

#print(f.readline())
#print(f.readline())
#print(f.readline(2))

#print(f.readlines())

for line in f.readlines():
     print(line)

f.close()