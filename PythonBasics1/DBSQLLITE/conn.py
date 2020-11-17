import sqlite3
# import cx_Oracle

def getConn():
    # return cx_Oracle.connect('krishna/oracle@localhost:1521/xe')
    return sqlite3.connect("myTable.db")

#crsr.execute(sql_command,(24, "Rishabh1", "Bansal", "M", "2014-03-28"))
#except cx_Oracle.DatabaseError as e:

"""


Oracle:
-----------------------------------------
for woking with oracle db 
-> install cx_Oracle package
command: pip install cx_Oracle
 import cx_Oracle
 con = cx_Oracle.connect('krishna/oracle@localhost:1521/xe')
 

Mysql:
------------------
-> install mysql-connector
command: pip install mysql-connector
 import MySQLdb
con = MySQLdb.connect("localhost","testuser","testpassword","gfgdb" )
 



Sqllite:
---------------
import sqlite3

for db operations we need
-> connection obj
-> cursor obj


python     ----------->  Connection obj + cursor obj ------------------> Database
                           [ C  R  U  D ]
C - Create
R - Read
U - Update
D - Delete
                           
            
for sqllite3
-----------------------------
import sqlite3

Expectation : 
->Table , column :      
-> Row:
-> basic Sql queries ( insert/update/delete/read..etc.)
                 
steps:
1.Get connection
2.Get cursor 
use cursor obj for executing queries ( Insert, delete, Select , update)

3.1 FOR INSERT/UPDATE/DELETE 
call cursor.execute(<sql here>)  method

3.2 For reading sigle row
a) call cursor.execute(<sql here>)  method
b) cursor.fetchone() method

3.3. For reading multiple rows
a) call cursor.execute(<sql here>)  method
b) cursor.fetchall() method

4.commit transaction
connection.commit()

5.close connection
connection.close()
"""
def executeQuery(sql,data):
    rows = 0
    con = getConn()
    cursor = con.cursor()
    print("conn success")
    cursor.execute(sql,data)
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