import re
"""
[]	A set of characters
ATLEAST ONE OF THE CHAR EXISTS :


[0123]	Returns a match where any of the specified digits (0, 1, 2, or 3) are present
[arn]	Returns a match where one of the specified characters (a, r, or n) are present	
[a-n]	Returns a match for any lower case character, alphabetically between a and n	
[0123]	Returns a match where any of the specified digits (0, 1, 2, or 3) are present	
[0-9]	Returns a match for any digit between 0 and 9	
[0-5][0-9]	Returns a match for any two-digit numbers from 00 and 59	
[a-zA-Z]	Returns a match for any character alphabetically between a and z, lower case OR upper case

[^arn]	Returns a match for any character EXCEPT a, r, and n	

only [_.,!] Returns a match where any of the specified match is found
[0-39] is the same as [01239]
[^abc] means any character except a or b or c
[^0-9] means any non-digit character.
"""

"""
string should contain either 0 or 1 or 2 or 3
"""


pattern = "[0123]";

test_strings = ['hi123bye', '111', '9999', '5ggrrg', 'gg6']

for testStr in test_strings:
  result = re.match(pattern, testStr)

  if result:
    print(testStr, " - valid successful.")
  else:
    print(testStr, " -Invalid.")

