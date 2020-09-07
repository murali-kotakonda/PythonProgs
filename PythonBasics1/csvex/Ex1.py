import csv

"""
Write to CSV:
-------------------
STEP1:

1.create file object  -> mention filname
2. CREATE csvwriter OBJECT using file obj
3. USE writerow()   -> 1 row , i/p:tuple
  OR writerows() -> multiple rows i/p:tuple of tuples

"""

# field names
fields = ['Name', 'sub1', 'sub2', 'sub3', 'sub4']

# data rows of csv file
rows = [['user1', '20', '30', '50','80'],['user2', '40', '100', '90','80']]

# writing to csv file
with open("students.csv", 'w4', newline='') as f:
    # creating a csv writer object
    csvwriter = csv.writer(f)
    #csvwriter = csv.writer(f,delimiter='#')

    # writing the fields
    csvwriter.writerow(fields)

    # writing the data rows
    csvwriter.writerows(rows)

print("write to csv success")