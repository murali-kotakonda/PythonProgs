import re


"""
allow digits only 1 to 5
"""




pattern = "[1-5]";

test_strings = ['hi123bye', 'Apple', 'cat', '---B---', '1313','!@#!#!#!#','6789']

for testStr in test_strings:
  result = re.search(pattern, testStr)

  if result:
    print(testStr, " - valid successful.")
  else:
    print(testStr, " -Invalid.")

