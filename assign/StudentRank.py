#Find the rank for given studnet Name , sub1 , sub2 , sub3
#take size as input : 3
# user1 70 , 80 90
# user2 100 90 100
# user3 100 80 70
# from assign.Util import big
# big(highMarks,total)

size = int(input("enter no of students"))
rankName =""
highMarks=0
for i in range(size):
    name = input("enter student name")
    sub1 = int(input("enter sub1"))
    sub2 = int(input("enter sub2"))
    sub3 = int(input("enter sub3"))
    total = sub1 +sub2 +sub3
    if(total>highMarks):
        highMarks = total
        rankName =name

print(highMarks)
print(rankName)
     
    