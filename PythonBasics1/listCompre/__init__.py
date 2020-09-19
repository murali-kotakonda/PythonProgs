# Variable
# Expression for output
# Reference sequence
# Predicate (Optional)

#Ex1
print("numbers square")
mylist = [1, 2, 3, 4, 5, 6]

output =[]
for number in mylist:
    output.append(number * number)
print(output)
"""
Variable -> number
Expression  -> number * number
Reference -> mylist
"""
# approach2
print("********************square of every number*******************************")
#output =  [ <expression> for <variable> in <Reference>]
output = [(number * number) for number in mylist]
print(output)

#Ex2
mylist = [1, 2, 3, 4, 5, 6]
print("********************add each num in second number*******************************")
output = [(number) for number in mylist]
print(output)

#Ex3
mylist = [1, 2, 3, 4, 5, 6]
print("********************double of  each num in second number*******************************")
output = [(number * 2) for number in mylist]
print(output)

output = [(number + 1) for number in mylist]
print(output)

#Ex4
#split the word in sentence and add to list
word = "Python#hana#sap#hana"
words = []
for occur in word.split("#"):
    words.append(occur)
print(words)


word = "Python#hana#sap#hana"
words = [occur for occur in word.split("#")]
print(words)

#add upper for every word
list_string = ['maNgo', 'BanAna', 'PytHoN iS Love', 'my Name IS Kumar']
upperList = [word.upper() for word in list_string]
print(upperList)


pow2 = [x*x for x in range(11)]
print(pow2)

#even Nos
myList = [1, 2, 3, 4, 5, 6]
evenList = [(number) for number in myList if number % 2 == 0]
print(evenList)

#Odd Nos
myList = [1, 2, 3, 4, 5, 6]
oddList = [(number) for number in myList if number % 2 != 0]
print(oddList)

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