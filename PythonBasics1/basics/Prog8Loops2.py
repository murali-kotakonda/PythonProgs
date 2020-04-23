# take size as input and perform the sum for the entered numbers


s = 0
while (s < 100):
    num = int(input("enter num"))
    if (num > 0):
        s = num + s
print("sum of num=", s)

s = 0
while (s < 100):
    num = int(input("enter num"))
    if (num < 0):
        continue
    s = num + s
print("sum of num=", s)

s = 0
while (s < 100):
    num = int(input("enter num"))
    if (num < 0):
        continue
    if (num == 999):
        break
        s = num + s
print("sum of num=", s)

# TAKE INT AS INPUTS CONTINUOSLY , AND PERFORM SUM , IF THE SUM  >= 50 stop and print
sum= 0
 
while sum <50:
    i = int(input('enter number'))
    sum= sum+i;
    print("current sum =",sum)
 
print(sum)


# TAKE INT AS INPUTS CONTINUOSLY , AND PERFORM SUM , IF THE SUM  >= 50 stop and print , if negative num --> dont sum 
sum= 0
while sum <50:
    i = int(input('enter number'))
    if i<0 :
        continue # take you to next iternation  by stopping curren iteration
    sum= sum+i;
    print("current sum =",sum)
 
print(sum)


# TAKE INT AS INPUTS CONTINUOSLY , AND PERFORM SUM , IF THE SUM  >= 50 stop and print , if negative num --> stop algorithm , and  display current sum 
sum= 0
while sum <50:
    i = int(input('enter number'))
    if i<0 :
        break # stop all iterations and come out of the loop
    sum= sum+i;
    print("current sum =",sum)

print(sum)


# we can write the else block for a while loop
sum= 0
while sum <50:
    i = int(input('enter number'))
    if i<0 :
        break # stop all iterations and come out of the loop
    sum= sum+i;
    print("current sum =",sum)
else : # executes ocne the loop is done
     print(sum)



