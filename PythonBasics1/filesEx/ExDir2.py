import os

os.chdir('C://test')
print(os.getcwd())

for f in os.listdir('C:\\'):
    # f_name, f_ext = os.path.splitext(f)
    if os.path.isdir(f) :
        print("folder name", f)

    if os.path.isfile(f):
        print("file name", f)

out = os.path.dirname('C://test')
print("base :: ", out)