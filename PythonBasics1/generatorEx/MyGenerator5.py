def changeUpper(str):
    length = len(str);
    for i in str:
        yield i.upper()


for ch in changeUpper("India"):
    print(ch, end="")

print("\n")
for ch in changeUpper("Hi user1 HOW are You"):
    print(ch, end="")
  