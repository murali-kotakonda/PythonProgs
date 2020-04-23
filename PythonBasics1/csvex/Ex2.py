import csv

myData = [
        {'Name': 'User1', 'sub1': '100', 'sub2': '90', 'sub3': '80'},
        {'Name': 'User2', 'sub1': '100', 'sub2': '90', 'sub3': '80'},
        {'Name': 'User3', 'sub1': '100', 'sub2': '90', 'sub3': '80'},
        {'Name': 'User4', 'sub1': '100', 'sub2': '90', 'sub3': '80'},
        {'Name': 'User5', 'sub1': '100', 'sub2': '90', 'sub3': '80'}
         ]

# headers
fields = ['Name', 'sub1', 'sub2', 'sub3']

# name of csv file
filename = "students1.csv"

# writing to csv file
with open(filename, 'w',newline='') as csvfile:
    # creating a csv dict writer object
    writer = csv.DictWriter(csvfile, fieldnames=fields)

    # writing headers (field names)
    writer.writeheader()

    # writing data rows
    writer.writerows(myData)







import csv

with open('names.csv', 'w') as csvfile:
    fieldnames = ['first_name', 'last_name']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
    writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
    writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})


