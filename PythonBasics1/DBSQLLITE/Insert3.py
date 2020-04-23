from conn import getConn


con =getConn()
cursor = con.cursor()
print("conn success")
sql = """INSERT INTO PERSON VALUES({} ,'{}' , {} , {})""".format( 6124,'raj kumar4',35,5000)
cursor.execute(sql)
con.commit()
print(cursor.rowcount, "record inserted.")
print("1 record inserted, ID:", cursor.lastrowid)
if cursor:
  cursor.close()
if con:
   con.close()

