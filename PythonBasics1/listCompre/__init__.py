#List comprehension:
#we have a list/tuple/colection using which we need to create a new collection by applying some
# sort filtering or manipulating

# Variable
# Expression for output
# Reference sequence
# Predicate (Optional)


# Ex1 perform square of every num and store in a new list
print("numbers square")

mylist = [1, 2, 3, 4, 5, 6]

# Approach1
output = []
for number in mylist:
    output.append(number * number)

print(output)

# Approach2
"""
Reference -> mylist
Expression  -> number * number
Variable -> number  [Every num in list]
"""

#syntax:
# output =  [ <expression> for <variable> in <Reference>]

output = [(number * number) for number in mylist]
print(output)







#Ex2
print("********************add each num in second number*******************************")
mylist = [1, 2, 3, 4, 5, 6]
output = [(number) for number in mylist]
print(output)




#Ex3
print("********************double of  each num in second number*******************************")
mylist = [1, 2, 3, 4, 5, 6]

output = [(number * 2) for number in mylist]
print(output)

output = [(number + 1) for number in mylist]
print(output)

#Ex4
# split the word in sentence and add to list
word = "Python#hana#sap#java"

# Approach1
words = []
for occur in word.split("#"):
    words.append(occur)

print(words)

# Approach2
words = [occur for occur in word.split("#")]
print(words)




#add upper for every word
list_string = ['maNgo', 'BanAna', 'PytHoN iS Love', 'my Name IS Kumar']
upperList = [word.upper() for word in list_string]
print(upperList)

#square of 1st 10 nums
print("square of 1st 10 nums")
pow2 = [x*x for x in range(11)]
print(pow2)




myList = [1, 2, 3, 4, 5, 6,7,8,10,20,24,25,27,19,30]

#even Nos
evenList = [  num for num in myList  if number % 2 == 0  ]
print(evenList)

#Odd Nos
oddList = [  num for num in myList  if num % 2 != 0  ]
print(oddList)

#add divisble by 5
list = [  num for num in myList  if num % 5 == 0  ]
print(list)



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