import csv
import os
import qrcode


csvDataFile = input('\nPlease enter the csvFile: ')

""" Manejo del archivo con datos que seran codificados """


file = open(csvDataFile)
csvreader = csv.reader(file)
header = []
header = next(csvreader)
rows = []

""" creación de directorio asociado con archivo de entrada para almacenamiento de códigos generados
 """
parent_dir = "./codesQR"
carpeta = csvDataFile[7:15]
path = os.path.join(parent_dir,carpeta)
os.mkdir(path)

""" iteracion que recorre cada una de las filas del archivo de entrada y genera 
codigo QR correspondiente a la información
 """
 
for row in csvreader:
    # row.append(csvDataFile[7:10]) # Agrega a la file un segmento de String de la ruta del archivo
    img = qrcode.make(row)
    img.save(f'{path}/qr{row[0]}.png')

