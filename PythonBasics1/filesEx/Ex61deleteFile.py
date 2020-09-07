import os
"""

# check if file exits
os.path.exists("user.txt")  # returns boolean

#Delete file
 os.remove("user.txt")
 
 
"""


if os.path.exists("user.txt"):
    print("deleting")
    os.remove("user.txt")
else:
    print("file not found")
