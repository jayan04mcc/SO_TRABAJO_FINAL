import threading
import tkinter as tk
import time
class Proceso: # definimos la clase
    def __init__(self, nombre, tiempo_llegada, duracion):
        self.nombre = nombre
        self.tiempo_llegada = tiempo_llegada
        self.duracion = duracion #tiempo en la cpu
        self.tiempo_inicio = None
        self.tiempo_finalizacion = None

procesos = [
    Proceso("P1", 0, 4),
    Proceso("P2", 28, 3),
    Proceso("P3", 12, 1),
    Proceso("P4", 3,2),
    Proceso("P5", 14,7),
    Proceso("P6", 95,3),
    Proceso("P7",1,2)
]
def eliminar_primer_elemento():
    # Verificar si la lista tiene elementos
    if listbox.size() > 0:
        # Eliminar el primer elemento de la lista
        listbox.delete(0)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title('Eliminar Primer Elemento')

# Crear el Listbox
listbox = tk.Listbox(ventana)
listbox.pack(padx=10, pady=10)

# Insertar algunos elementos en el Listbox
elementos = ["Elemento 1", "Elemento 2", "Elemento 3", "Elemento 4"]
for elemento in procesos:
    listbox.insert(tk.END, f"{elemento.nombre} -Llegada: {elemento.tiempo_llegada}")

# Crear un botón para eliminar el primer elemento
boton_eliminar = tk.Button(ventana, text="Eliminar Primer Elemento", command=eliminar_primer_elemento)
boton_eliminar.pack(padx=10, pady=10)


# Ejecutar el bucle principal de la ventana
ventana.mainloop()
