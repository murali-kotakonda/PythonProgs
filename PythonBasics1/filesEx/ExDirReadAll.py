import os 
  
# This is to get the directory that the program is currently running in.
dir_path = os.path.dirname(os.path.realpath(__file__)) 
  
for root, dirs, files in os.walk(dir_path):
    for file in files:  
        if file.endswith('.txt'): 
            print(root+'/'+str(file))


"""
Read all the files/folders recursively for the given folder name:

"""
for root, dirs, files in os.walk("C:\\test"):
    print("**************************",root,"************************")
    print(dirs)
    print(files)


