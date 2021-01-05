import re

"""
  USAGE OF *
  python followed by any NUMBER OF X
  
"""
pattern = "python*X";


test_strings = ['python', 'pythonX', 'pythonXXX', 'abcX', 'abonX','Z6789','hi hi hi hi']


for testStr in test_strings:
  result = re.match(pattern, testStr)

  if result:
    print(testStr, " - valid successful.")
  else:
    print(testStr, " -Invalid.")

