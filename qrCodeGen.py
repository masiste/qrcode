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
    row.append(csvDataFile[7:9]) # Agrega a la file un segmento de String de la ruta del archivo
    img = qrcode.make(row)
    img.save(f'./codesQR/11-1/qr{row[0]}.png')

