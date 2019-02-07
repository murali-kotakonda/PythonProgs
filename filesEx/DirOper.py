import os


print(os.name)

print(os.getcwd())

#print(os.listdir("c://"))
print(os.listdir())

os.mkdir("test5")

os.rename("test5","test6")

os.rmdir("test6")


print(os.listdir("C://"))


isFile = os.path.isfile("Ex1.py")
print(isFile)


isDir = os.path.isdir("test")
print(isDir)