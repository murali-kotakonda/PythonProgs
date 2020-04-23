import sqlite3
# import cx_Oracle

def getConn():
    # return cx_Oracle.connect('krishna/oracle@localhost:1521/xe')
    return sqlite3.connect("myTable.db")

#crsr.execute(sql_command,(24, "Rishabh1", "Bansal", "M", "2014-03-28"))
#except cx_Oracle.DatabaseError as e:


def executeQuery(sql):
    rows = 0
    con = getConn()
    cursor = con.cursor()
    print("conn success")
    cursor.execute(sql)
    con.commit()

    print(cursor.rowcount, "record inserted.")
    print("1 record inserted, ID:", cursor.lastrowid)
    rows = cursor.rowcount
    if cursor:
        cursor.close()
    if con:
        con.close()
    return rows


"""
Mysql
--------------
python -m pip install mysql-connector
import mysql.connector


oracle:
-------
pip install  cx_Oracle
import cx_Oracle

"""