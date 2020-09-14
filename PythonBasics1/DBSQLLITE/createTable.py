"""

Table : PERSON
columns:
id
name
age
salary

SQL: 
CREATE TABLE PERSON (  
			ID INTEGER PRIMARY KEY,  
			NAME VARCHAR(20),  
			AGE INTEGER,  
			SALARY INTEGER
  );


"""
import sqlite3

# connecting to the database
con = sqlite3.connect("myTable.db")

# cursor
cursor = con.cursor()

# SQL command to create a table in the database
sql_command = """CREATE TABLE PERSON (  
ID INTEGER PRIMARY KEY,  
NAME VARCHAR(20),  
AGE INTEGER,  
SALARY INTEGER);"""

# execute the statement
cursor.execute(sql_command)
con.commit()

print("table create success...")
# close the connection
if cursor:
   cursor.close()
if con:
   con.close()