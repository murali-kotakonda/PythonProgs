import os

if os.path.exists("test2.txt"):
    os.remove("test2.txt")
    print("file deleted")
else:
    print("file doesnt not exists ")    

