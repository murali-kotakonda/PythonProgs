
'''
Created on Aug 20, 2018

@author: I335484
'''
def changeUpper(str):
    length = len(str);
    print(length)
    for i in range(length - 1, -1, -1):
        yield str[i]


for ch in changeUpper("India"):
    print(ch)
  