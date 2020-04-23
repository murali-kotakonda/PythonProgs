'''
Created on Aug 6, 2018

@author: i335484
'''

if __name__ == '__main__':
    pass

f = open("test.txt", "w")

f.write("hello1\r")
f.write("user1\n")
f.write("how are you1")

f.close();

f = open("test.txt", "a")

f.write("hello1\r")
f.write("user\n")
f.write("how are you")

f.close();

try:
   f =open("test.txt","w")
   f.write("hello\r")
   f.write("user\n")
   f.write("how are you")
except IOError:
    print("invalid file operations");
else:
    print("success")
finally:
    print("handle any resources..")
    f.close();
    