#from Module3  call m4() function:


from PythonBasics1.modulesext import Module3
#from <pkg> import <file>
Module3.m4("kumar")


import PythonBasics1.modulesext.Module3 as MyMod
#import <pkg>.<filename> as <alias>
MyMod.m4("user1")



from PythonBasics1.modulesext.Module3 import m4
#import <pkg>.<filename> import <function>
m4("add")