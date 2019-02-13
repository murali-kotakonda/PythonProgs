"File operations"

"""Opening a file 
specify file name + mode [ "r"  ,"w"  "a" ,"x" , "r+"]

open with x  attribute will create the file, if the file exists it gives exception
f = open("user.txt","x")
"""

"""open with w  attribute 
a) if file exists , then start write the contnet
b) if file doesnt exists , then create file."""

f = open("user.txt", "w")
if f.mode == 'w':
    f.write("hi\n")
    f.write("hello")
    
if f.closed==False:    
    f.close()

f1 = open("user.txt", "a")
f1.write("muralidhar")
f1.close()

