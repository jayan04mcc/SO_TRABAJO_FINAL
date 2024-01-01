import tkinter as tk
from fcfs_algorithm import Proceso, FCFS
import time

def actualizar_listbox(listbox, elementos):
    listbox.delete(0, tk.END)
    for elemento in elementos:
        listbox.insert(tk.END, elemento)

def iniciar_simulacion(procesos, listbox_cola, listbox_cpu, ventana):
    for estado_cola, estado_cpu in FCFS(procesos):
        actualizar_listbox(listbox_cola, [f"{p.nombre} - Llegada: {p.tiempo_llegada}" for p in estado_cola])
        actualizar_listbox(listbox_cpu, [f"{p.nombre} - Finaliza: {p.tiempo_finalizacion}" for p in estado_cpu])
        ventana.update()
        time.sleep(5)  # Ajusta este tiempo según la velocidad que desees para la simulación

def crear_interfaz():
    ventana = tk.Tk()
    ventana.geometry("800x400")
    ventana.title("Simulación FCFS")
    
    listbox_cola = tk.Listbox(ventana)
    listbox_cola.place(x=50, y=50, width=300, height=300)

    listbox_cpu = tk.Listbox(ventana)
    listbox_cpu.place(x=450, y=50, width=300, height=300)

    procesos = [
    Proceso("P1", 0, 4),
    Proceso("P2", 1, 3),
    Proceso("P3", 2, 1),
    Proceso("P4", 3,2),
    Proceso("P5", 4,7),
    Proceso("P6", 5,3),
    Proceso("P7",6,2)
]
    boton_iniciar = tk.Button(ventana, text="Iniciar Simulación", command=lambda: iniciar_simulacion(procesos, listbox_cola, listbox_cpu, ventana))
    boton_iniciar.place(x=350, y=10)

    return ventana
