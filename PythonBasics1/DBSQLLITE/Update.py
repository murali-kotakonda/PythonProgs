from conn import getConn

# connecting to the database
con = getConn()

# cursor
cursor = con.cursor()


# SQL command to insert the data in the table
sql_command = "UPDATE PERSON SET NAME = ? WHERE Id=?"
cursor.execute(sql_command,("suchi",26))

# To save the changes in the files. Never skip this.
# If we skip this, nothing will be saved in the database.
con.commit()
print(cursor.rowcount, "record updated.")
# close the connection
con.close()