import re

"""
  USAGE OF *
  python followed by any DIGIT
  
"""
pattern = "python?[0-9]";


test_strings = ['python$1','python1', 'python13131', 'n121', 'abcX', 'abonX','Z6789','hi hi hi hi']


for testStr in test_strings:
  result = re.match(pattern, testStr)

  if result:
    print(testStr, " - valid successful.")
  else:
    print(testStr, " -Invalid.")

