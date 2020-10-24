"""
read from list and write to file
	use writelines() method

"""
f =None
try:
    list = ["a line of text\n", "another line of text\n", "a third line\n", "kumar\n", "ram\n"]
    f =open("test.txt", "w")
    f.writelines(list)
except IOError:
    print("invalid file operations");
else:
    print("success")
finally:
    print("handle any resources..")
    f.close()
    