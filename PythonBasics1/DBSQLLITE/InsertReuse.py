from conn import executeQuery

rows = executeQuery("INSERT INTO PERSON VALUES(699,'raj kumada4',35,5000)")
if(rows==1):
        print("insert success")
else:
        print("insert fail")
