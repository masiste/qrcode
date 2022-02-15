
import cv2

decoder = cv2.QRCodeDetector()

file_name="qr1011399435.png"
image = cv2.imread(file_name)
link, data_points, straight_qrcode = decoder.detectAndDecode(image)
print(id)
