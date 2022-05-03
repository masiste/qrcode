import csv
import os
import qrcode


csvDataFile = input('\nPlease enter the csvFile: ')

file = open(csvDataFile)
csvreader = csv.reader(file)
header = []
header = next(csvreader)
rows = []

parent_dir = "./codesQR"
carpeta = csvDataFile[7:12]
path = os.path.join(parent_dir,carpeta)
os.mkdir(path)

for row in csvreader:
    # row.append(csvDataFile[7:10]) # Agrega a la file un segmento de String de la ruta del archivo
    img = qrcode.make(row)
    img.save(f'{path}/qr{row[0]}.png')

