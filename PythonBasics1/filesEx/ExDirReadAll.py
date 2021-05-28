

"""
Read all the files/folders recursively for the given folder name:

use os.walk("C:\\test") function

"""
import os

for root, dirs, files in os.walk("C:\\test"):
    print("**************************",root,"************************")
    print(dirs)
    print(files)


