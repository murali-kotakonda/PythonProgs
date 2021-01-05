import re
"""
  end with bye
"""
pattern ="bye$"


test_strings =  ['hi kumar bye' ,'hi kumar byeeeeeeeeee','hi kumar sffffffffffffbye', ]

for testStr in test_strings:
  result = re.search(pattern, testStr)

  if result:
    print(testStr, " - valid successful.")
  else:
    print(testStr, " -Invalid.")