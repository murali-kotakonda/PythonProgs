"""
1.take number as input
print numbers from 1 till input.

ex: if input is 90
o/p: orint from 1 to 90


2. dispalay numbers from 90 to 1


2.take number as input
print all even numbers till input

3.take number as input
print all odd numbers till input

4.take number as input
print multiplication table


5.take size as input
then takes numbers for size no of times.
and
find 1.sum 2.big 3. small

ex:
enter size : 4
enter n1 : 30
enter n2 : 40
enter n3 : 50
enter n4 : 20

o/p:
sum : 140
big : 50
small : 20


6. sum of nunmbers from 1 to 90



"""

# Write a Python program to construct the following pattern, using a nested for loop.
# 
# * 
# * * 
# * * * 
# * * * * 
# * * * * * `
# * * * * 
# * * * 
# * * 
# *





n=5;
for i in range(n):
    for j in range(i):
        print ('* ', end="")
    print('')

for i in range(n,0,-1):
    for j in range(i):
        print('* ', end="")
    print('')

    """
I/p: 5

1
1 2
1 2 3
1 2 3 4
1 2 3 4 5


i/p:5
5 4 3 2 1 
5 4 3 2
5 4 3 
5 4 
5


i/p:5
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15  


i/p:5
o/p:
* 
* * 
* * * 
* * * * 
* * * * * `
* * * * 
* * * 
* * 
*


    
    """