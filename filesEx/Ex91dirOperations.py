import os
import os.path
import struct
from os import path

#This function gives the name of the operating system dependent module imported. 
#The following names have currently been registered: ‘posix’, ‘nt’, ‘os2’, ‘ce’, ‘java’ and ‘riscos’
print(os.name) 
print(os.getcwd())
print(os.listdir())

os.mkdir("test5")
#os.chdir("test5")
#os.rename('test5','test56')
os.rmdir("test5")

os.listdir('C:\\')


# For 32 bit it will return 32 and for 64 bit it will return 64
print(struct.calcsize("P") * 8)
#check file exists
def main():
   print ("file exist:"+str(path.exists('guru99.txt')))
   print ("File exists:" + str(path.exists('career.guru99.txt')))
   print ("directory exists:" + str(path.exists('myDirectory')))
   print ("Is it File?" + str(path.isfile('guru99.txt')))
   print ("Is it File?" + str(path.isfile('myDirectory')))
   print ("Is it Directory?" + str(path.isdir('guru99.txt')))
   print ("Is it Directory?" + str(path.isdir('myDirectory')))
main()




#Python program to get OS name, platform and release information.
import platform
import os
print(os.name)
print(platform.system())
print(platform.release())

 