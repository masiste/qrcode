# qrcode
## Programs by generated qr codes

Al intentar correr el programa qrCode.py despliega un error
Se activa un entorno virtual con los comandos

Creando entorno virtual e instalando paquetes necesarios

    carpeta>python3 -m venv venv_qrcode  -->  para crear carpeta del entorno virtual
    carpeta>source venv_qrcode/bin/activate   -->  para activar el entorno virtual

Instalacion de paquetes al interior del entorno virtual creado

     pip install qrcode   -->  genera codigos QR 
     pip install pillow   -->  para manejo de imagenes

Guardar codigos generados al interior de la carpeta del proyecto con la ruta

    ./codesQR/code QR.png  --> con referencia al directorio actual del proyecto

Los codigos QR generados son etiquetados segun el nombre del archivo ingresado utilizando el numero de documento y el grupo al que pertenece el estudiante para realizar el codigo QR
