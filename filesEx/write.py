f = open("test.txt","a")

str = ""
while str!="bye":
    str = input("entr str")
    f.write(str)

f.close()