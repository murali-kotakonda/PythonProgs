from conn import getConn

con =getConn()
cursor = con.cursor()
print("conn success")
sql1 = "SELECT * FROM person where NAME=? "
data1 = ["26"]
cursor.execute(sql1, data1)

row = cursor.fetchone()

for columnValue in row:
   print(columnValue)

if cursor:
  cursor.close()
if con:
  con.close()


  """
  
#Get all details whose id is 26

sql1 = "SELECT * FROM person where ID=? "
data1 = ["26"]
cursor.execute(sql1, data1)
row = cursor.fetchone()

for columnValue in row:
   print(row)
 
  """


