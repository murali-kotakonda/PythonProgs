import os 
# 
# OS.walk() generate the file names in a directory tree by walking the tree either top-down or bottom-up. For each directory in the tree rooted at directory top (including top itself), 
# it yields a 3-tuple (dirpath, dirnames, filenames).
# This is to get the directory that the program  
# is currently running in. 
dir_path = os.path.dirname(os.path.realpath(__file__)) 

for root, dirs, files in os.walk(dir_path):
     print(root)
     print(dirs)
     print (files) 
