'''
Created on Aug 6, 2018

@author: i335484
'''

if __name__ == '__main__':
    pass


try:
    f =open("test.txt", "a")
    f.write("my new data added ");
except IOError:
    print("invalid file operations");
else:
    print("success")
finally:
    print("handle any resources..")
    f.close();
    