import csv
from email import header
import qrcode


csvDataFile = input('\nPlease enter the csvFile: ')

file = open(csvDataFile)
csvreader = csv.reader(file)
header = []
header = next(csvreader)
rows = []

for row in csvreader:
    row.append(csvDataFile[0:2])
    img = qrcode.make(row)
    img.save(f'./codesQR/qr{row[0]}.png')

