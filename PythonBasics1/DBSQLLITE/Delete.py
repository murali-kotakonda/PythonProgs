from conn import getConn

# connecting to the database
connection = getConn()

# cursor
crsr = connection.cursor()


# SQL command to insert the data in the table
sql_command = """DELETE FROM PERSON WHERE Id=?"""
crsr.execute(sql_command,[24])

connection.commit()
print(crsr.rowcount, "record DELETED.")
# close the connection
connection.close()