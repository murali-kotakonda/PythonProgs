from conn import getConn

con =getConn()
cursor = con.cursor()
print("conn success")
sql1 = "SELECT * FROM person where NAME=? "
data1 = ["Kumar23"]
cursor.execute(sql1, data1)

myresult = cursor.fetchone()

for row in myresult:
   print(row)

if cursor:
  cursor.close()
if con:
  con.close()