from conn import getConn

# connecting to the database
connection = getConn()

# cursor
crsr = connection.cursor()


# SQL command to insert the data in the table
sql_command = """UPDATE PERSON SET NAME = ? WHERE Id=?"""
crsr.execute(sql_command,("suchi",24))

# To save the changes in the files. Never skip this.
# If we skip this, nothing will be saved in the database.
connection.commit()
print(crsr.rowcount, "record updated.")
# close the connection
connection.close()