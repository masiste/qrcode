import qrcode

def qr_code():
 user_data = input("\nPlease enter the data you want inside your QR Code:")
 img = qrcode.make(user_data)
 img.save('./codesQR/QR Code.png')
 img.show()
 print(type(user_data))
 print('\nQR Code Generated\n')

qr_code()

