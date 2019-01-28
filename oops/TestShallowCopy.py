import copy


p = ['user1','user2','user4']

#p1=p
p1 = copy.copy(p)

print("*********p data*******")
print(p)
print("*********p1 data*******")
print(p1)

p1.append('user2000')

print("*********p data*******")
print(p)
print("*********p1 data*******")
print(p1)

