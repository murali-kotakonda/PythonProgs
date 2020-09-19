#add 1 to 100 to list using list comprehension

#add even no  from 2 to 500 in a list
a = [i for i in range(1, 100)]
print(a)

a = [i for i in range(2, 100, 2)]
print(a)

a = [i for i in range(1, 100, 2)]
print(a)

x = [int(z) for z in input("Enter multiple numbers: ").split()]
print("input numbers are: ", x)

x = [str(z) for z in input("Enter multiple strings: ").split()]
print("input strings are: ", x)

x = [float(z) for z in input("Enter multiple floats: ").split()]
print("input floats are: ", x)


