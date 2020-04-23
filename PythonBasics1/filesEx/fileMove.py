# Python program to move
# files
import shutil

# Source path
source = "Test4.txt"

# Destination path
destination = "D:\test\Test\G"

# Move the content of
# source to destination
dest = shutil.move(source, destination)

print("move success")
# print(dest) prints the
# Destination of moved directory