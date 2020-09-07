import os 



os.rename("user1.txt","helo.txt")



os.chdir('C://test')
print(os.getcwd())

for f in os.listdir():
    f_name, f_ext = os.path.splitext(f)
    f_name = f_name + "1"

    new_name = '{} {}'.format(f_name, f_ext)
    os.rename(f, new_name)