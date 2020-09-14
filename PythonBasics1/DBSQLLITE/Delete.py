from conn import getConn

# connecting to the database
con = getConn()

# cursor
cursor = con.cursor()


# Delete the row whose id is 26
sql_command = """DELETE FROM PERSON WHERE Id=?"""
cursor.execute(sql_command,[26])

con.commit()
print(cursor.rowcount, "record DELETED.")
# close the connection
con.close()