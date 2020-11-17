from conn import getConn

# connecting to the database
con = getConn()

# cursor
cursor = con.cursor()


# SQL command to insert the data in the table
sql = """INSERT INTO PERSON VALUES (?,?,?,?)"""
cursor.execute(sql,(26, "Rishabh1", 89,1313))
con.commit()
print(cursor.rowcount, "record inserted.")


# close the connection
con.close()