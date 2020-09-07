#Earlier
f= open("test.txt", "w")
f.write("Hello World!!!")
f.write("Bye!!!")
f.close()

#Now
with open("test.txt", "w") as f:
    f.write("Hello World!!!")
    f.write("Bye!!!")