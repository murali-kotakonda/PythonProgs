"""

SELECT * FROM person   -> Get all rows and all  columns values
SELECT ID,NAME  FROM person -> Get all rows and fetch only ID,NAME  column values
SELECT * FROM person where ID=1212; -> Get  all  columns values for a row  whose ID = 1212
SELECT * FROM person where NAME='KUMAR'   -> Get  all  columns values for a row  whose NAME = KUMAR
SELECT ID FROM person where NAME='KUMAR' -> Get  Only Idcolumn value for a row  whose NAME = KUMAR

"""

from conn import getConn

con =getConn()
cursor = con.cursor()

print("conn success")

#Get all rows
cursor.execute("SELECT * FROM person")
rows = cursor.fetchall() # returns list of tuples
for row in rows:
  print(row)

if cursor:
    cursor.close()
if con:
    con.close()

""" 
# BAD EXAMPLES. DON'T DO THIS!
cursor.execute("SELECT admin FROM users WHERE username = '" + username + '");
cursor.execute("SELECT admin FROM users WHERE username = '%s' % username);
cursor.execute("SELECT admin FROM users WHERE username = '{}'".format(username));
cursor.execute(f"SELECT admin FROM users WHERE username = '{username}'");
"""


"""
Best approach
cursor.execute("SELECT admin FROM users WHERE username = %s'", (username, ));
cursor.execute("SELECT admin FROM users WHERE username = %(username)s", {'username': username});

"""