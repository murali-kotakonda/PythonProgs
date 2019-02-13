import os.path, time
print("Last modified: %s" % time.ctime(os.path.getmtime("test.txt")))
print("Created: %s" % time.ctime(os.path.getctime("test.txt")))



import os.path
import time

print('File         :', __file__)
print('Access time  :', time.ctime(os.path.getatime(__file__)))
print('Modified time:', time.ctime(os.path.getmtime(__file__)))
print('Change time  :', time.ctime(os.path.getctime(__file__)))
print('Size         :', os.path.getsize(__file__))