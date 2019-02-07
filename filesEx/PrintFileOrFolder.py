import os

print(os.getcwd())

os.chdir("C://test")

print(os.getcwd())

for f in os.listdir():
    print(f)
    print(os.path.isfile(f))