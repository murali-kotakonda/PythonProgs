import re
"""
start with hi and end with bye but 8chars
"""
pattern ="^hi...bye$"

test_string = 'hi123bye'
result = re.match(pattern, test_string)

if result:
  print("valid successful.")
else:
  print("Invalid.")