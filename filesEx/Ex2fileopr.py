def writeContent(f):
    if f.mode == 'w':
        f.write("hello")

    
f = open("user.txt", "r")
#f = open("C:/Python33/README.txt") 
writeContent(f)

print(f.mode)
print(f.closed)
print(f.name)
print(f.encoding) 
print(f.newlines) 
print(f.readable())
print(f.writable())

f.tell()    # get the current file position

f.seek(0)   # bring file cursor to initial position


