# Importamos las librerías necesarias
import tkinter as tk
import time

# Creamos la ventana principal
ventana = tk.Tk()
ventana.title("Reloj en Python")

# Creamos una etiqueta para mostrar la hora
reloj = tk.Label(ventana, font=("Arial", 40, "bold"), bg="black", fg="white")

# Colocamos la etiqueta en la ventana
reloj.pack()

# Definimos una función que actualiza la hora
def actualizar():
    # Obtenemos la hora actual
    hora = time.strftime("%H:%M:%S")
    # Actualizamos el texto de la etiqueta
    reloj.config(text=hora)
    # Llamamos a la función cada segundo
    reloj.after(1000, actualizar)

# Llamamos a la función por primera vez
actualizar()

# Iniciamos el bucle principal de la ventana
ventana.mainloop()
