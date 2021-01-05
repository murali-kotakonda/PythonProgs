import re


"""
string should contain only alphabets upper or lower
"""


pattern = "[a-zA-Z]";

test_strings = ['hi123bye', 'Apple', 'cat', '---B---', '1313','!@#!#!#!#']

for testStr in test_strings:
  result = re.search(pattern, testStr)

  if result:
    print(testStr, " - valid successful.")
  else:
    print(testStr, " -Invalid.")

