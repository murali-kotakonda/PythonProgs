"""
Loops/iterations:
-> execute same code but on different data for multiple runs until condition is satisfied.

python supports :
1.For loop
2.While loop

for is  block where the code  for body should be written with tab space.
for loop has 3 sections:
1.init
2.condition
3.increment/decerment
=> while loop only condition is mandatory

when should i use for loop?
ans) when we know the number of iterations/runs
     when we are looping the collections like list,tuple,dict
     
when should i use while loop? 
ans)
when we dont know the number of iterations/runs.


"""


"""
for is a block so : is required at the end of for statement
use indentation or tab space for writing the code


"""
#Print Hello for 20 times
print("***************************Print Hello for 20 times****************************************")
for i in range(20):
    print("Hello")
"""
1. init : i=0
2. condition : i<20
3. increment : i =i +1
"""

print("***************************Print numbers from 1  for 50 ****************************************")
for i in range(1,51):  # prints from 1 to 50
    print(i)
"""
1.  init : i=1
2.condition : i<51
3.increment : i = i+1
"""

print("***************************Print numbers  starts with 3 till 50 increment by 4 ****************************************")
for i in range(3,50,4):
    print(i)
"""
1. init :  i=3
2. condition :  i<51
3. increment :   i = i+4
"""



"""

here i is variable
range() is the function
                     init   condition   increment
range(50)        :    0       <50         +1
range(2,50)      :    2       <50         +1
range(4, 50, 3)  :    4       <50         +3




                         init           condition         increment
range(20)                  0               <20               +1
range(2,51)                2               <51               +1
range(3,50,4)              3               <50               +4
"""











# i is the counter variable ,
# i starts from zero
# deafult increment is 1
# condition is i < 5
# range() is a buuiltin funtion , range specifies till what number

"""
for i in range(5):
    print("hello")

"""





"""
for i in range(20):
    print(i)

for i in range(3, 20):
    print(i)

for i in range(5, 20, 3):
    print(i)


i = 0
while (i < 5):
    print("Hello")
    i = i + 1

# 0 to 9 ( init 0 , condi < 10, incre +1)
for i in range(10):
    print(i)

# 2 to  9 ( init 2, cond < 10 , incre +1)
for i in range(2, 10):
    print(i)

i = 2
while (i < 10):
    print(i)
    i = i + 1

# 2 , 7, 12  ( init 2 , < 60 , incre +5)
for i in range(2, 60, 5):
    print(i)

i = 2
while (i < 60):
    print(i)
    i = i + 5

"""
