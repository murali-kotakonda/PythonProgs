
"""
files:
--------------

for working with files we need os module.


create folder
rename folder
del folder


create file
del file
write to file
read from file


file obj represents both file and folder.


ex: import os
 


"""

import os

import struct
from os import path
"""
import os
from os import path

create a folder
os.mkdir("<folder name>")


how to check if folder exists:
os.path.exists("<folder name>") # returs boolean


How to remove a folder:
os.rmdir("<folder name>")


How to rename the folder:
os.rename('<old folder name>', '<new folder name>')

 
"""


# create a folder
import os.path
if not os.path.exists("test5"):
    os.mkdir("test5")

# rename a folder
import os.path
os.rename('test5', 'test56')

# remove a folder
import os.path
os.rmdir("test56")



os.chdir("test5")
#print(os.listdir())




