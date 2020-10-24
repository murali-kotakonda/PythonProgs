"""
write to a file.

use write() function to write string to file
"""
f = open("user.txt", "w")

f.write("hello1 kumar\n")
f.write("user1\n")
f.write("how are you1")

print("write success")
f.close()

