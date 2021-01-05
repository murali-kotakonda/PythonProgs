import re

"""
any character except a or b or c
"""

pattern = "[^abc]";

test_strings = ['hi123bye', 'Apple', 'cat', '---B---', '1313','!@#!#!#!#','6789']

for testStr in test_strings:
  result = re.match(pattern, testStr)

  if result:
    print(testStr, " - valid successful.")
  else:
    print(testStr, " -Invalid.")

