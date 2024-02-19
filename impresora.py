from win32 import win32print
from win32 import win32gui
import os
import win32ui

# Obtener el nombre de la impresora predeterminada
printer_name = win32print.GetDefaultPrinter()
# Crear un contexto de dispositivo para la impresora
printer = win32print.OpenPrinter(printer_name)
print(printer)
devmode = win32print.GetPrinter(printer, 2)["pDevMode"]
dc = win32gui.CreateDC("WINSPOOL", printer_name, devmode)
# Iniciar un documento con el nombre "Imprimir archivos"
docinfo = ("DocName", "Imprimir archivos")
# win32print.StartDoc(dc, docinfo)

# Obtener la lista de los archivos en la carpeta Clase_1
archivos = os.listdir("imagenes/train/Clase_1")

# Recorrer la lista e imprimir cada archivo
for archivo in archivos:
    # Abrir el archivo en modo binario
    f = open(os.path.join("imagenes/train/Clase_1", archivo), "rb")
    # Leer el contenido del archivo
    contenido = f.read()
    
    # Cerrar el archivo
    f.close()
    # Iniciar una página
    win32print.StartPage(dc)
    # Enviar el contenido del archivo a la impresora
    win32print.WritePrinter(dc, contenido)
    # Terminar la página
    win32print.EndPage(dc)

# Terminar el documento
win32print.EndDoc(dc)

# Cerrar el contexto de dispositivo
win32print.ClosePrinter(printer)
