#assignmnets

a=b=c=100
print(a,b,c)

a,b,c =100,200,300
print(a,b,c)

a,b,c = 100, 12.2424, "krishna"
print(a,b,c)



print("***********print with seperator********************")
a,b,c =100,200,300
print(a,b,c, sep ="$")# seperator for every value. default seperator is single space" "
#what should be the printed after every  value

print("***********print with end********************")
print(a , end="***")  # what should be the printed after the last value , default is "\n"
print(b , end="***")
print(c , end="***")
print("hello", "python",)


print("***********print with sep and end********************")
print(a ,b, c ,sep="#" ,end="***")
print("bye")




print("***********print values ************************")
"""
o/p:
a =  100 , b = 200 , c = 300

req: print combining multiple variables and values 
use the place holder approach.
"""


a,b,c= 70,90,80
print( "a = " , a  , "b = " , b , "c = ", c)
print("student 1 mark  = {} , student 2 mark= {} , student 3 mark= {} ".format(a,b,c))













