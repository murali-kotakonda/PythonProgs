#EARLIER
#----------------------------------------------------------------------------
#use below code for multiple inputs
x,y,z  = input("Enter multiple value: ").split()
print(x, type(x))
print(y,type(x))
print(z,type(x))

#convert x , y , z to the int 



#NOW
#----------------------------------------------------------------------------------
myInput =  [   int(x) for x in   input("Enter multiple value: ").split()           ]

print(type(myInput))

for i in myInput:
   print(i , type(i))





