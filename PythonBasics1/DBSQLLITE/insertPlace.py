from conn import getConn

con =getConn()
cursor = con.cursor()
print("conn success")

cursor.execute("INSERT into PERSON values (%d, '%s', %d, %d )"%(6008, 'raj kumar1', 35, 5000))
con.commit()
print(cursor.rowcount, "record inserted.")
print("1 record inserted, ID:", cursor.lastrowid)

if cursor:
   cursor.close()
if con:
   con.close()

