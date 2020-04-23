import os



if os.path.exists("user.txt"):
    print("deleting")
    os.remove("user.txt")
else:
    print("file not found")
