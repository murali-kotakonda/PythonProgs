import re
"""
start with hi and end with bye
"""
import re

pattern = "^hi.*bye$"

test_strings = ['hi kumar bye', 'aadhi kumar byeeeeeeeeee', 'hi kumar sffffffffffffbye', ]

for testStr in test_strings:
  result = re.match(pattern, testStr)

  if result:
    print(testStr, " - valid successful.")
  else:
    print(testStr, " -Invalid.")
