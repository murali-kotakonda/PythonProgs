"""
#List comprehension:
#short hand notation for creating the target list using the source list

- It has 4 sections:
# Variable
# Expression for output
# Reference sequence
# Predicate (Optional)

I/p: is  list/tuple/collection
O/p : list/tuple/collection  by applying some filtering or manipulating logic

adv:
----
- reducing the number of lines of code
- simple code for manipulating the list/tuple

 
"""

  
# Ex1 perform square of every num and store in a new list
print("numbers square")

mylist = [1, 2, 3, 4, 5, 6]

print("********************Approach 1**************************")
# Approach1
output = []

for num in mylist:  # get every num from 1st list
    res =  num * num  # perform square of each number
    output.append(res)   # add to the 2nd list

print(output)

print("********************Approach 2**************************")

"""
Reference -> mylist
Expression  -> num * num
Variable -> num  [Every num in list]

output =  [ <expression> for <variable> in <Reference>]

"""

output1 =  [ num * num for num in mylist]
print(output1)








#Ex2
print("********************add each num from 1st list and add to second list*******************************")
mylist = [1, 2, 3, 4, 5, 6]
output = [(number) for number in mylist]
print(output)




#Ex3
print("********************double of  each num in second list*******************************")
mylist = [1, 2, 3, 4, 5, 6]

output = [(number * 2) for number in mylist]
print(output)

output = [(number + 1) for number in mylist]
print(output)

#Ex4
# split the word in sentence and add to list
word = "Python#hana#sap#java"


print("********************Approach 1**************************")
words = []
for occur in word.split("#"):
    words.append(occur)

print(words)


print("********************Approach 2**************************")


output1 =  [ occur for occur in word.split("#")]
print(output1)




#add upper for every word
list_string = ['maNgo', 'BanAna', 'PytHoN iS Love', 'my Name IS Kumar']
upperList = [word.upper() for word in list_string]
print(upperList)

#square of 1st 10 nums
print("square of 1st 10 nums")
pow2 = [x*x for x in range(11)]
print(pow2)




mylist = [1, 2, 3, 4, 5, 6,7,8,10,20,24,25,27,19,30]

print("************************even Nos*****************************")
#create a new list with even Nos
output1 =  [ num  for num in mylist if num%2==0]
print(output1)


print("************************Odd Nos*****************************")
#create a new list with Odd Nos
output1 =  [ num  for num in mylist if num%2!=0]
print(output1)



print("************************numbers divisble by 5*****************************")
#create a new list with numbers divisble by 5
output1 =  [ num  for num in mylist if num%5==0]
print(output1)







#ferquency of every word in the list
string_words ="python java hana sap java sap python"
word_list = string_words.split()
word_count_freq = [word_list.count(n) for n in word_list]
print(word_count_freq)

print("String:\n {} \n".format(string_words))
print("List:\n {} \n".format(str(word_list)))

print(list(zip(word_list, word_count_freq)))
print("Pairs (Words and Frequencies:\n {}".format(str(list(zip(word_list, word_count_freq)))))

#ferquency of every word in the list
string_words ="python java hana sap java sap python"
word_list = string_words.split()
word_count_freq = set([ n +  "_"+str(word_list.count(n)) for n in word_list])
print(word_count_freq)