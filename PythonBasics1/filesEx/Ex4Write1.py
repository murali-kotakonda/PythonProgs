"""
Req : write to a file.

steps:
1.open file
2.write the content
3.close the file

use write() function to write string to file
"""

f = open("user.txt", "w")

f.write("hello1 kumar\n")
f.write("user1\n")
f.write("how are you1")

print("write success")
f.close()

