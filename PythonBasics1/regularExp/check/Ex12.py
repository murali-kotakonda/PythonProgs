import re

"""
 EITHER C or P allowed
"""
pattern = "C|P";


test_strings = ['Chi123bye', 'AppleC', 'cat', '---P---', '1313','!@#!#!#!#','6789','hi123hibye','hii','hi hi hi hi']


for testStr in test_strings:
  result = re.search(pattern, testStr)

  if result:
    print(testStr, " - valid successful.")
  else:
    print(testStr, " -Invalid.")

