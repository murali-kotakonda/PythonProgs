import cx_Oracle

# Create a table in Oracle database
cursor = None
con = None
try:

    con = cx_Oracle.connect('krishna/oracle@localhost:1521/xe')

    # Now execute the sqlquery
    cursor = con.cursor()

    print("conn success")

    format_str = """INSERT INTO Person VALUES ({id}, '{name}', {age}, {sal})"""

    sql_command = format_str.format(id=2001, name='Kumar23', age=87 , sal=1224)
    print(sql_command)
    cursor.execute(sql_command)
    con.commit()

    print(cursor.rowcount, "record inserted.")
    print("1 record inserted, ID:", cursor.lastrowid)
except cx_Oracle.DatabaseError as e:
    print("There is a problem with Oracle", e)

# by writing finally if any error occurs
# then also we can close the all database operation
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
 