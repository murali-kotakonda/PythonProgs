list = ["sap","sap","java","kumar","dotnet","sap","kumar","java"]

d =dict()

for word in list:
    if word in d.keys():
        count = d[word]
        count = count+1
        d.update({word:count})
    else:
        d.update({word: 1})

print(d)