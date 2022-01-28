import qrcode


def qr_code(rowFile):
    
    img = qrcode.make(rowFile)
    img.save('./codesQR/QR Code.png')
    


