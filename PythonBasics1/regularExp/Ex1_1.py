import re
"""
start with hi  
"""
pattern ="^hi"

test_string = 'hi  kumar bye'
result = re.match(pattern, test_string)

if result:
  print("valid successful.")
else:
  print("Invalid.")