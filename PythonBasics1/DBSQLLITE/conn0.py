"""
How to get the connection obj for sqlite
the database is stored in the "myTable.db" file.

"""

import sqlite3

#get conn obj
con = sqlite3.connect("myTable.db")

#get cursor obj
cursor = con.cursor()
print("conn success")


#close conn and cursor
if cursor:
   cursor.close()
if con:
   con.close()

