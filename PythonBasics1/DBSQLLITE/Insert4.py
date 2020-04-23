from conn import getConn


con =getConn()
cursor = con.cursor()
print("conn success")
sql = """INSERT INTO Person VALUES ({id}, '{name}', {age}, {sal})"""
sql_command = sql.format(id=2001, name='Kumar23', age=87, sal=1224)
cursor.execute(sql_command)
con.commit()
print(cursor.rowcount, "record inserted.")
print("1 record inserted, ID:", cursor.lastrowid)
if cursor:
  cursor.close()
if con:
   con.close()