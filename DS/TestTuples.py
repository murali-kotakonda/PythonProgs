myTuple = ("krishna", 19087, 76655.113131)

print(type(myTuple))
print(myTuple)

#serach by index: folows index baseds operations

print(myTuple[0])
print(myTuple[2])
#print(myTuple[3]) # run time exception


#myTuple[0] = "user3"; # exception as modifucation to tuple is not applicable


#slicing
print(myTuple[0:2]) # start from position 0 and display two elements
print(myTuple[-1]) #  prints the last element


#trepeat
print(myTuple*2)


#concat
myTuple1 =  ('1','2')
newTuple = myTuple + myTuple1;
print(newTuple)


#length of tuple
print(len(myTuple))

#serach by content
print('user1' in myTuple)
print('krishna' in myTuple)

#iterate the tuple
for i in range(len(myTuple)):
    print(myTuple[i])
 