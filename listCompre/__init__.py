# Variable
# Expression for output
# Reference sequence
# Predicate (Optional)

word = "Python"
letters = []
for letter in word:
    letters.append(letter)
print(letters)






word = "Python"
letters = [letter for letter in word]
print(letters)




reference = [1, 2, 3, 4, 5, 6]
output = [(number) for number in reference if number % 2 == 0]
print(output)



list_string = ['maNgo', 'BanAna', 'PytHoN iS Love', 'Cat iS not doG']
list_of_list = [sentence.upper() for sentence in list_string]
print(list_of_list)




pow2 = [2 ** x for x in range(10)]
print(pow2)


string_words =""
word_list = string_words.split()

word_freq = [word_list.count(n) for n in word_list]

print("String:\n {} \n".format(string_words))
print("List:\n {} \n".format(str(word_list)))
print("Pairs (Words and Frequencies:\n {}".format(str(list(zip(word_list, word_freq)))))
