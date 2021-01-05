import re

"""
hi should appear miniumum 1 and max 2
"""
pattern = "hi{1,2}";


test_strings = ['hi123bye', 'Apple', 'cat', '---B---', '1313','!@#!#!#!#','6789','hi123hibye','hii','hi hi hi hi']


for testStr in test_strings:
  result = re.search(pattern, testStr)

  if result:
    print(testStr, " - valid successful.")
  else:
    print(testStr, " -Invalid.")

