from conn import getConn

# connecting to the database
con = getConn()

# cursor
cursor = con.cursor()


# SQL command to insert the data in the table
sql_command = """DELETE FROM PERSON WHERE Id=?"""
cursor.execute(sql_command,[24])

con.commit()
print(cursor.rowcount, "record DELETED.")
# close the connection
con.close()