#The open() function takes two parameters; filename, and mode.
# "r" - Read - Default value. Opens a file for reading, error if the file does not exist
# 
# "a" - Append - Opens a file for appending, creates the file if it does not exist
# 
# "w" - Write - Opens a file for writing, creates the file if it does not exist
#
# "x" - Create - Creates the specified file, returns an error if the file exists

# In addition you can specify if the file should be handled as binary or text mode
# 
# "t" - Text - Default value. Text mode
# 
# "b" - Binary - Binary mode (e.g. images)

f = open("demofile.txt") 
#or
f = open("demofile.txt", "rt")



# 
# To open the file, use the built-in open() function.
# 
# The open() function returns a file object, which has a read() method for reading 
# the content of the file:

"""
Read Only (‘r’) : Open text file for reading. The handle is positioned at the beginning of the file. If the file does not exists, raises I/O error. This is also the default mode in which file is opened.
Read and Write (‘r+’) : Open the file for reading and writing. The handle is positioned at the beginning of the file. Raises I/O error if the file does not exists.
Write Only (‘w’) : Open the file for writing. For existing file, the data is truncated and over-written. The handle is positioned at the beginning of the file. Creates the file if the file does not exists.
Write and Read (‘w+’) : Open the file for reading and writing. For existing file, data is truncated and over-written. The handle is positioned at the beginning of the file.
Append Only (‘a’) : Open the file for writing. The file is created if it does not exist. The handle is positioned at the end of the file. The data being written will be inserted at the end, after the existing data.
Append and Read (‘a+’) : Open the file for reading and writing. The file is created if it does not exist. The handle is positioned at the end of the file. The data being written will be inserted at the end, after the existing data.
"""
