a=b=c=10
print(a,b,c)

a,b=6,7
print(a,b)

a,b =10,"hi"
print(a,b)


a,b,c =10,"hi",12.344

print("**************print in same line**************")
print(a,b,c)



print("**************print in new line**************")
print(a,b,c,sep="\n")



print("**************print seperate by # **************")
print(a,b,c,sep="#")

print("**************print end by space**************")
print(a,end="  ")
print(b,end="  ")
print(c,end="  ")



a=6
b=8
b+=a # -,*,/ , //,
print(b)
