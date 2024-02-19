# Importamos las librerías necesarias
import tkinter as tk
import time

# Creamos la ventana principal
ventana = tk.Tk()
ventana.title("Cronómetro en Python")

# Creamos una variable para almacenar el tiempo inicial
inicio = 0

# Creamos una variable para almacenar el tiempo actual
actual = 0

# Creamos una variable para almacenar el estado del cronómetro
corriendo = False

# Creamos una función para actualizar la etiqueta del tiempo
def actualizar():
    global inicio, actual, corriendo
    if corriendo:
        # Calculamos el tiempo transcurrido
        actual = time.time() - inicio
        # Formateamos el tiempo en horas, minutos y segundos
        horas = int(actual // 3600)
        minutos = int((actual % 3600) // 60)
        segundos = int(actual % 60)
        # Actualizamos el texto de la etiqueta
        tiempo.config(text=f"{horas:02d}:{minutos:02d}:{segundos:02d}")
    # Llamamos a la función cada 100 milisegundos
    ventana.after(100, actualizar)

# Creamos una función para iniciar el cronómetro
def iniciar():
    global inicio, actual, corriendo
    if not corriendo:
        # Marcamos el tiempo inicial
        inicio = time.time() - actual
        # Cambiamos el estado del cronómetro
        corriendo = True

# Creamos una función para pausar el cronómetro
def pausar():
    global inicio, actual, corriendo
    if corriendo:
        # Cambiamos el estado del cronómetro
        corriendo = False

# Creamos una función para reiniciar el cronómetro
def reiniciar():
    global inicio, actual, corriendo
    # Reseteamos el tiempo inicial y actual
    inicio = 0
    actual = 0
    # Cambiamos el estado del cronómetro
    corriendo = False
    # Actualizamos el texto de la etiqueta
    tiempo.config(text="00:00:00")

# Creamos una etiqueta para mostrar el tiempo
tiempo = tk.Label(ventana, font=("Arial", 40, "bold"), bg="black", fg="white")
tiempo.pack()

# Creamos un marco para los botones
botones = tk.Frame(ventana)
botones.pack()

# Creamos los botones de iniciar, pausar y reiniciar
iniciar = tk.Button(botones, text="Iniciar", command=iniciar)
iniciar.grid(row=0, column=0, padx=5, pady=5)

pausar = tk.Button(botones, text="Pausar", command=pausar)
pausar.grid(row=0, column=1, padx=5, pady=5)

reiniciar = tk.Button(botones, text="Reiniciar", command=reiniciar)
reiniciar.grid(row=0, column=2, padx=5, pady=5)

# Llamamos a la función de actualizar por primera vez
actualizar()

# Iniciamos el bucle principal de la ventana
ventana.mainloop()