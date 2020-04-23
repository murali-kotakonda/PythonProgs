from conn import getConn

# connecting to the database
connection = getConn()

# cursor
crsr = connection.cursor()


# SQL command to insert the data in the table
sql_command = """INSERT INTO PERSON VALUES (?,?,?,?)"""
crsr.execute(sql_command,(26, "Rishabh1", 89,1313))

connection.commit()
print(crsr.rowcount, "record inserted.")
# close the connection
connection.close()