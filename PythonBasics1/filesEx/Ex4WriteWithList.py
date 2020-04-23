'''
Created on Aug 6, 2018

@author: i335484
'''

if __name__ == '__main__':
    pass


try:
    f =open("test.txt","w")
    lines_of_text = ["a line of text\n", "another line of text\n", "a third line"]
    f.writelines(lines_of_text)
except IOError:
    print("invalid file operations");
else:
    print("success")
finally:
    print("handle any resources..")
    f.close();
    