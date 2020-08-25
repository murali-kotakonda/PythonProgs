import os
import time

# 
# OS.walk() generate the file names in a directory tree by walking the tree either top-down or bottom-up. For each directory in the tree rooted at directory top (including top itself), 
# it yields a 3-tuple (dirpath, dirnames, filenames).
# This is to get the directory that the program  
# is currently running in. 
dir_path = os.path.dirname(os.path.realpath(__file__)) 

for root, dirs, files in os.walk("C:\\Users\\i335484\\OneDrive - SAP SE\\Desktop"):
     print(root)
     print(dirs)
     print (files)

     for f1 in files:
          f1 = root+"\\"+f1
          f = open(f1)
          print(f.closed)
          print(f.name)
          print(f.encoding)
          print(f.newlines)
          print(f.readable())
          print(f.writable())

          print("Last modified: %s" % time.ctime(os.path.getmtime(f1)))
          print("Created: %s" % time.ctime(os.path.getctime(f1)))

          print('File         :', f)
          print('Access time  :', time.ctime(os.path.getatime(f1)))
          print('Modified time:', time.ctime(os.path.getmtime(f1)))
          # print('Change time  :', time.ctime(os.path.getctime(__file__))) run un unix
          print('Size         :', os.path.getsize(f1))
          print("Created: %s" % time.ctime(os.path.getctime(f1)))
          print(f.mode)
          print(f.closed)
          print(f.name)
          print(f.encoding)
          print(f.newlines)
          print(f.readable())
          print(f.writable())

          print("Last modified: %s" % time.ctime(os.path.getmtime(f1)))
          print("Created: %s" % time.ctime(os.path.getctime(f1)))

          print('File         :', f)
          print('Access time  :', time.ctime(os.path.getatime(f1)))
          print('Modified time:', time.ctime(os.path.getmtime(f1)))
          # print('Change time  :', time.ctime(os.path.getctime(__file__))) run un unix
          print('Size         :', os.path.getsize(f1))
          print("Created: %s" % time.ctime(os.path.getctime(f1)))
          f.close()
