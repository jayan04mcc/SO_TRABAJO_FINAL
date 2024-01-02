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
# Variable global para rastrear las ejecuciones
ejecuciones = 0

def show(listbox, elementos):
    global ejecuciones  # Usar la variable global 'ejecuciones'
    while ejecuciones <=1:
    # Si el hilo ingresa por segunda vez
        if ejecuciones == 1:
            listbox.delete(0, tk.END)
            elementos.sort(key=lambda x: x.tiempo_llegada)
        
        for elemento in elementos:
            listbox.insert(tk.END,f"{elementos[0].nombre} -TimeEjec: {elementos[0].duracion}")

            listbox.insert(tk.END, f"{elemento.nombre} -Llegada: {elemento.tiempo_llegada}")
            time.sleep(1)
        
        # Incrementar el contador de ejecuciones
        ejecuciones += 1

# Crear la ventana principal
root = tk.Tk()

# Crear el Listbox
listbox = tk.Listbox(root)
listbox.pack()

print(len(procesos))
# Crear y comenzar un hilo para agregar los elementos
hilo = threading.Thread(target=show, args=(listbox,procesos))
hilo.start()

# Iniciar el ciclo de eventos
root.mainloop()
