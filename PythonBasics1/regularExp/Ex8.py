
import re


"""
 Matches any decimal digit. Equivalent to [0-9]
 
 \d Matches any decimal digit. Equivalent to [0-9]
 \s Matches where a string contains any whitespace character. Equivalent to [ \t\n\r\f\v]
 \w Matches any alphanumeric character (digits and alphabets). Equivalent to [a-zA-Z0-9_]
"""

pattern = "\d";

test_strings = ['hi123bye', 'Apple', 'cat', '---B---', '1sddgf','1313','!@#!#!#!#','6789']

for testStr in test_strings:
  result = re.match(pattern, testStr)

  if result:
    print(testStr, " - valid successful.")
  else:
    print(testStr, " -Invalid.")

