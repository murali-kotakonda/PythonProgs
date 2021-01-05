import re


"""
string should contain atleast any character from A TO M
"""


pattern = "[A-M]";

test_strings = ['hi123bye', 'Apple', 'cat', '---B---', 'gg6']

for testStr in test_strings:
  result = re.search(pattern, testStr)

  if result:
    print(testStr, " - valid successful.")
  else:
    print(testStr, " -Invalid.")

