import os 

os.chdir('C://test') 
print(os.getcwd()) 
  
for f in os.listdir(): 
    f_name, f_ext = os.path.splitext(f) 
    print(f_name)
    print(os.path.isdir(f))
    print(os.path.isfile(f))
   

out = os.path.dirname('C://test') 
print("base :: ",out) 