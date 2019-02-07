#f = open("test.txt")

f = open("test.txt","w")  #r , a , w , x


print(f.mode)
print(f.closed)
print(f.name)
print(f.encoding)
print(f.readable())
print(f.writable())

f.close()