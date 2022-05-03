import csv

csvFile1 = input('\n Please enter the file 1:  ' )

file = open(csvFile1)
csvReader = csv.reader(file)
rows = []

for row in csvReader:
    print (row[1])
