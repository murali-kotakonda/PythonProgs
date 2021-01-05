import re

"""
 EITHER C or P allowed TO START WITH AND followed by digit
"""
pattern = "(C|P)[0-9]";


test_strings = ['C13131331', 'P13131331', 'a131313', '---P---', '!@#!#!#!#','Z6789','hi hi hi hi']


for testStr in test_strings:
  result = re.match(pattern, testStr)

  if result:
    print(testStr, " - valid successful.")
  else:
    print(testStr, " -Invalid.")

