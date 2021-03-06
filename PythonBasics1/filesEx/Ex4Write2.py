"""
write to an existing file.

use 'a' mode for writing from last file state.

'w'-> delete current file content and rewrites
'a' -> write from last content
use write() function to write string to file

"""
f = open("user.txt", "a")

f.write("hello1adad raj \n")
f.write("user111111ad\n")
f.write("where are youaddff")

print("write success")
f.close()



