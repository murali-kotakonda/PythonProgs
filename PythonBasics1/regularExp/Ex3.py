import re
"""
start with hi and end with bye but 8chars
"""
pattern ="^hi...bye$"

test_strings =  ['hi123bye' ,'hi kumar bye','hibye','abcdefgh','hiabcbye' ]

for testStr in test_strings:
  result = re.match(pattern, testStr)

  if result:
    print(testStr, " - valid successful.")
  else:
    print(testStr, " -Invalid.")