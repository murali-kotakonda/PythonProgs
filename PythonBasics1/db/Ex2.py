import cx_Oracle

# Create a table in Oracle database
cursor = None
con = None
try:

    con = cx_Oracle.connect('krishna/oracle@localhost:1521/xe')

    # Now execute the sqlquery
    cursor = con.cursor()

    print("conn success")

    cursor.execute("SELECT * FROM person")

    myresult = cursor.fetchall()

    for x in myresult:
        print(x)

except cx_Oracle.DatabaseError as e:
    print("There is a problem with Oracle", e)

# by writing finally if any error occurs
# then also we can close the all database operation
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()