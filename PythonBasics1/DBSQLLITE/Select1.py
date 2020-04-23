from conn import getConn

con =getConn()
cursor = con.cursor()
print("conn success")
cursor.execute("SELECT * FROM person")
myresult = cursor.fetchall()
for x in myresult:
  print(x)

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