import os

"""
Read the files/folders in a given folder
Hint:
os.path.isdir(f)  -> to check whether the content is a folder
os.path.isfile(f)  -> to check whether the content is a file
os.listdir('C:\\test')  -> returns the list of content in the folder

"""
import os
os.chdir('C:\\test')
for f in os.listdir('C:\\test'):
    # f_name, f_ext = os.path.splitext(f)
    if os.path.isdir(f) :
        print("folder name", f)

    if os.path.isfile(f):
        print("file name", f)


"""

print(os.getcwd())


out = os.path.dirname('C://test')
print("base :: ", out)
"""