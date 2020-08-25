import sqlite3
# import cx_Oracle



con = sqlite3.connect("myTable.db")
cursor = con.cursor()
print("conn success")
#cursor.execute(sql)
#con.commit()

if cursor:
   cursor.close()
if con:
   con.close()

