import tkinter as tk
import time
from collections import deque
class Proceso:
    def __init__(self, nombre, tiempo_llegada, duracion):
        self.nombre = nombre
        self.tiempo_llegada = tiempo_llegada
        self.duracion = duracion
        self.tiempo_inicio = None
        self.tiempo_finalizacion = None

procesos = [
    Proceso("P1", 0, 4),
    Proceso("P2", 1, 3),
    Proceso("P3", 2, 1),
    Proceso("P4", 3,2),
    Proceso("P5", 4,7),
    Proceso("P6", 5,3),
    Proceso("P7",6,2)
]
# Crear la ventana principal
ventana = tk.Tk()
ventana.geometry("800x400")
ventana.title("Simulación FCFS")

# Crear el Listbox para la cola de procesos
listbox_cola = tk.Listbox(ventana)
listbox_cola.place(x=50, y=50, width=300, height=300)

# Crear el Listbox para la CPU
listbox_cpu = tk.Listbox(ventana)
listbox_cpu.place(x=450, y=50, width=300, height=300)
def show_now(listbox,elementos):
    listbox.delete(0, tk.END)
    for elemento in elementos:
        listbox.insert(tk.END, elemento)

def actualizar_listbox(listbox, elementos):
    listbox.delete(0, tk.END)
    for elemento in elementos:
        listbox.insert(tk.END, elemento)

def fcfs(procesos):
    procesos.sort(key=lambda x: x.tiempo_llegada)
    cola = deque(procesos)
    tiempo_actual = 0
    procesos_en_cpu = []

    while cola or procesos_en_cpu:
        # Actualizar la cola de procesos
        while cola and cola[0].tiempo_llegada <= tiempo_actual:
            procesos_en_cpu.append(cola.popleft())

        if procesos_en_cpu:
            
            proceso_actual = procesos_en_cpu.pop(0)
            
            tiempo_actual = max(tiempo_actual, proceso_actual.tiempo_llegada) + proceso_actual.duracion
            proceso_actual.tiempo_finalizacion = tiempo_actual
            print(f"Proceso: {proceso_actual.nombre}, Tiempo de Inicio: {proceso_actual.tiempo_llegada}, Tiempo de Finalizacion: {proceso_actual.tiempo_finalizacion}")

        # Actualizar los Listbox
        actualizar_listbox(listbox_cola, [f"{p.nombre} - Llegada: {p.tiempo_llegada}" for p in cola])
        actualizar_listbox(listbox_cpu, [f"{p.nombre} - Finaliza: {p.tiempo_finalizacion}" for p in procesos_en_cpu])

        # Simular el tiempo de procesamiento
        ventana.update()
        time.sleep(1)  # Ajusta este tiem

boton_iniciar = tk.Button(ventana, text="Iniciar Simulación", command=lambda: fcfs(procesos))
boton_iniciar.place(x=350, y=10)

# Iniciar la aplicación
ventana.mainloop()