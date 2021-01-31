
import os.path
import time
import os.path, time


def writeContent(f):
    if f.mode == 'w':
        f.write("hello")
#f = open("C:/Python33/README.txt") 
#writeContent(f)

#to create file os.chdir('C:\\test')
f = open("user.txt", "w")

print(f.mode)
print(f.closed)
print(f.name)
print(f.encoding) 
print(f.newlines) 
print(f.readable())
print(f.writable())

print("Last modified: %s" % time.ctime(os.path.getmtime("user.txt")))
print("Created: %s" % time.ctime(os.path.getctime("user.txt")))

print('Size         :', os.path.getsize(f.name))



print('File         :', __file__)
print('Access time  :', time.ctime(os.path.getatime(__file__)))
print('Modified time:', time.ctime(os.path.getmtime(__file__)))
#print('Change time  :', time.ctime(os.path.getctime(__file__))) run un unix
print('Size         :', os.path.getsize(__file__))
print("Created: %s" % time.ctime(os.path.getctime(__file__)))

#print("Created: %s" % time.ctime(os.path.getctime("test.txt")))

f.tell()    # get the current file position
f.seek(5)   # bring file cursor to initial position
f.close()


#os.path.getctime() method in Python is used to get system’s ctime of the specified path. Here ctime refers to the last metadata change for specified path in UNIX while in Windows, it refers to path creation time.