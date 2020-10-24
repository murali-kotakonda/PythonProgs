"""
write using exception handling

"""
f = None
try:
   f =open("user.txt", "w")
   f.write("hello\r")
   f.write("user\n")
   f.write("how are you")
except IOError:
    print("write failed....")
    print("invalid file operations")
else:
    print("write success")
finally:
    print("handle any resources..")
    f.close()