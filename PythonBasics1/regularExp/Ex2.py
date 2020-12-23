import re
"""
start with hi and end with bye
"""
pattern ="^hi.*bye$"

test_string = 'hi kumar bye'
result = re.match(pattern, test_string)

if result:
  print("valid successful.")
else:
  print("Invalid.")