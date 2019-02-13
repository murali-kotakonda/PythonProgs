list = [10, 5, 6, 8, 9]
genObj = (i ** 3 for i in list)

for i in genObj:
   print(i)