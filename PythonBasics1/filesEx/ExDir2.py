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