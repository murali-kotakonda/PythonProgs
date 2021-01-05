import re

"""
#expect two digits from the given input 
# allow only 0-5



"""
 
#pattern = "hi{1,2}";
pattern = "[0-5]{2}";

test_strings = ['hi123bye', 'Apple', 'cat', '---B---', '1313','!@#!#!#!#','6789','hi123hibye','hii','hi hi hi hi']

test_strings = ['1','99','11111']


for testStr in test_strings:
  result = re.search(pattern, testStr)

  if result:
    print(testStr, " - valid successful.")
  else:
    print(testStr, " -Invalid.")

