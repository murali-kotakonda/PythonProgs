
with open("test.txt","a") as f:
    f.write("writinmg with with()")
    
with open("test.txt","r") as f:
    for line in f.readlines():
     print(line)

#print(f.read())

#print(f.read(5))

#print(f.readline())
#print(f.readline())
#print(f.readline(2))

#print(f.readlines())

