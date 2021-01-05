import re

"""
any character except digits
"""
 
pattern = "[^0-9]";

test_strings = ['hi123bye', 'Apple', 'cat', '---B---', '1313','!@#!#!#!#','6789']

for testStr in test_strings:
  result = re.match(pattern, testStr)

  if result:
    print(testStr, " - valid successful.")
  else:
    print(testStr, " -Invalid.")

