"""
\d{3}
Match exactly 3 digits


\d{3,}
Match 3 or more digits

\d{3,5}
Match 3, 4, or 5 digits

python|perl
Match "python" or "perl"


rub(y|le))
Match "ruby" or "ruble"


Python(!+|\?)
"Python" followed by one or more ! or one ?


1
^Python
Match "Python" at the start of a string or internal line

2
Python$
Match "Python" at the end of a string or line

3
\APython
Match "Python" at the start of a string

4
Python\Z
Match "Python" at the end of a string

7
Python(?=!)
Match "Python", if followed by an exclamation point.

8
Python(?!!)
Match "Python", if not followed by an exclamation point.


\A	restricts the match to the start of string
\Z	restricts the match to the end of string
^	restricts the match to the start of line
$	restricts the match to the end of line
\n	newline character is used as line separator
re.MULTILINE or re.M	flag to treat input as multiline string
\b	restricts the match to the start/end of words
word characters: alphabets, digits, underscore
\B	matches wherever \b doesn't match


[aeiou]	Match any vowel
[^aeiou]	^ inverts selection, so this matches any consonant
[a-f]	- defines a range, so this matches any of abcdef characters
\d	Match a digit, same as [0-9]
\D	Match non-digit, same as [^0-9] or [^\d]
\w	Match word character, same as [a-zA-Z0-9_]
\W	Match non-word character, same as [^a-zA-Z0-9_] or [^\w]
\s	Match whitespace character, same as [\ \t\n\r\f\v]
\S	Match non-whitespace character, same as [^\ \t\n\r\f\v] or [^\s]


*	Match zero or more times
+	Match one or more times
?	Match zero or one times
{m,n}	Match m to n times (inclusive)
{m,}	Match at least m times
{,n}	Match up to n times (including 0 times)
{n}	Match exactly n times
pat1.*pat2	any number of characters between pat1 and pat2
pat1.*pat2|pat2.*pat1	match both pat1 and pat2 in any order






"""