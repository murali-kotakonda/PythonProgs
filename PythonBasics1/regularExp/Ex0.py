"""
Regular expressions:
----------------------

-> simple and best way to validate the data

expression:
-specifies the expected format for the data

packge : regular exppression
to work with "regular exppressio" , import re module



re.match() checks for a match only at the beginning of the string,
re.search() checks for a match anywhere in the string

"""


"""
^	Starts with
$	Ends with
.	Any character
*	Zero or more occurrences of the pattern left to it
+	one  or more occurrences of the pattern left to it

ma*n

mn	1 match
man	1 match
maaan	1 match
main	No match (a is not followed by n)
woman	1 match

{n,m}. This means at least n, and at most m repetitions of the pattern left to it.

a{2,3}
[0-9]{2, 4} matches at least 2 digits but not more than 4 digits

Check if the string contains "a" followed by exactly two "l" characters:
x = re.findall("al{2}", txt)


Vertical bar | is used for alternation (or operator).
a|b match any string that contains either a or b


(a|b|c)xz match any string that matches either a or b or c followed by xz

\A - Matches if the specified characters are at the start of a string.
\Athe
the sun	Match
In the sun	No match



\b - Matches if the specified characters are at the beginning or end of a word.
bfoo
football	Match
a football	Match
afootball	No match

foo\b
the foo	Match
the afoo test	Match
the afootest	No match

\B - Opposite of \b. Matches if the specified characters are not at the beginning or end of a word.


\d - Matches any decimal digit. Equivalent to [0-9]
\D - Matches any non-decimal digit. Equivalent to [^0-9]

\s - Matches where a string contains any whitespace character.

\w - Matches any alphanumeric character (digits and alphabets). Equivalent to [a-zA-Z0-9_]
\w
12&": ;c 	3 matches (at 12&": ;c)
%"> !	No match

https://www.w3schools.com/python/python_regex.asp
"""



"""
search() vs. match()
Python offers two different primitive operations based on regular expressions: 

re.match() checks for a match only at the beginning of the string, 
while re.search() checks for a match anywhere in the string

For example:

>>>
>>> re.match("c", "abcdef")    # No match
>>> re.search("c", "abcdef")   # Match
<re.Match object; span=(2, 3), match='c'>
Regular expressions beginning with '^' can be used with search() to restrict the match at the beginning of the string:

>>>
>>> re.match("c", "abcdef")    # No match
>>> re.search("^c", "abcdef")  # No match
>>> re.search("^a", "abcdef")  # Match
<re.Match object; span=(0, 1), match='a'>
Note however that in MULTILINE mode match() only matches at the beginning of the string, whereas using search() with a regular expression beginning with '^' will match at the beginning of each line.

>>>
>>> re.match('X', 'A\nB\nX', re.MULTILINE)  # No match
>>> re.search('^X', 'A\nB\nX', re.MULTILINE)  # Match
<re.Match object; span=(4, 5), match='X'>
"""