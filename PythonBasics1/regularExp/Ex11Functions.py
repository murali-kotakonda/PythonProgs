import re
#The findall() function returns a list containing all matches.

"""
returns all the matches as a list

if 1 capture group is used, only its matches are returned
1+, each element will be tuple of capture groups
portion matched by pattern outside group won't be in output
"""

txt = "HELLO9 KUMAR 1 4 5 * sfhjsfj 8 & 2"
x = re.findall("\d", txt)
print(x)

print("********************************search FUNCTION*******************************")
"""
The search() Function
The search() function searches the string for a match, and returns a Match object if there is a match.

If there is more than one match, only the first occurrence of the match will be returned:
-> x.start() gives position number

"""

x = re.search("\d", txt)
print(x.start())


print("********************************split FUNCTION*******************************")


"""
The split() Function
The split() function returns a list where the string has been split at each match:
"""

x = re.split("\d", txt)
print(x)



print("********************************sub FUNCTION*******************************")
"""
The sub() Function
The sub() function replaces the matches with the text of your choice:
"""

print(txt)
x = re.sub("\d", "[]", txt)
print(x)


"""
The Match object has properties and methods used to retrieve information about the search, and the result:

.span() returns a tuple containing the start-, and end positions of the match.
.string returns the string passed into the function
.group() returns the part of the string where there was a match
"""

"""
Print the position (start- and end-position) of 
t+he first match occurrence.

The regular expression looks for any words that starts with an upper case "S":


search() vs. match()
Python offers two different primitive operations based on regular expressions: 

re.match() checks for a match only at the beginning of the string, 
while re.search() checks for a match anywhere in the string



"""

import re

txt = " 78987 hi my house no: #9065655 , pin: 89"
#x = re.search(r"\bS\w+", txt)
x = re.search("\d", txt)

print(x.span())
print(x.string)
print(x.group())

