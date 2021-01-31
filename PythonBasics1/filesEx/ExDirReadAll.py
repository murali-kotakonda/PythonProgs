import os 
  


"""
Read all the files/folders recursively for the given folder name:

"""
for root, dirs, files in os.walk("C:\\test"):
    print("**************************",root,"************************")
    print(dirs)
    print(files)


