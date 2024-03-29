"""

csv read :
-> using csvReader
-> using DictReader

"""

import csv

#file = open("students.csv", 'r', newline='')
# opening the CSV file
with open('students.csv', mode='r')as file:
    # reading the CSV file
    csvFile = csv.reader(file)

    # displaying the contents of the CSV file
    for lines in csvFile:
        print(lines)




import csv
with open('students.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['Name'], row['sub1'],row['sub2'],row['sub3'])


# opening the CSV file
with open('students.csv', mode='r') as file:
    # reading the CSV file
    csvFile = csv.DictReader(file)

    # displaying the contents of the CSV file
    for lines in csvFile:
        print(lines)







import csv
# csv file name
filename = "students.csv"

# initializing the titles and rows list
fields = []
rows = []

# reading csv file
with open(filename, 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)

    # extracting field names through first row
    fields = csvreader.next()


    # extracting each data row one by one
    for row in csvreader:
        rows.append(row)

        # get total number of rows
    print("Total no. of rows: %d" % (csvreader.line_num))

# printing the field names
print('Field names are:' + ', '.join(field for field in fields))

#  printing first 2 rows
print('\nFirst 3 rows are:\n')
for row in rows[:2]:
    # parsing each column of a row
    for col in row:
        print("%10s" % col),
    print('\n')