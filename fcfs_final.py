import tkinter as tk
import time
from collections import deque
from queue import Queue
import threading as th
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
ejecuciones =0
cont_cpu=1
ventana = tk.Tk()
ventana.geometry("800x400")
ventana.title("Simulación FCFS")

# Crear el Listbox para la cola de procesos
listbox_cola = tk.Listbox(ventana)
listbox_cola.place(x=50, y=50, width=300, height=300)

# Crear el Listbox para la CPU
listbox_cpu = tk.Listbox(ventana)
listbox_cpu.place(x=450, y=50, width=300, height=300)
def show(listbox, elementos):
    global ejecuciones  # Usar la variable global 'ejecuciones'
    while ejecuciones <=1:
        if ejecuciones == 1:
            listbox.delete(0, tk.END)
            elementos.sort(key=lambda x: x.tiempo_llegada)
        for elemento in elementos:
            listbox.insert(tk.END, f"{elemento.nombre} -Llegada: {elemento.tiempo_llegada}")
            time.sleep(1)
        # Incrementar el contador de ejecuciones
        ejecuciones += 1

def show_cpu(listbox,elementos):
    global cont_cpu
    procesos.sort(key=lambda x: x.tiempo_llegada)
    while cont_cpu<=len(elementos):
        listbox.insert(tk.END,f"{elementos[cont_cpu-1].nombre} -TimeEjec: {elementos[cont_cpu-1].duracion}")# trabajamos con la listbox cpu
        for i in range(elementos[cont_cpu-1].duracion):
            listbox.insert(tk.END,f"{i+1}...")
            time.sleep(0.5)
        time.sleep(1)
        listbox.delete(0, tk.END)
        if listbox_cola.size()>0:
            listbox_cola.delete(0)
            time.sleep(1)
        cont_cpu += 1
def show_multiple(listbox,listbox2,elementos):
    show(listbox, elementos)
    show_cpu(listbox2, elementos)

def algoritmo_fcfs(procesos):
    hilo1=th.Thread(target=show_multiple,args=(listbox_cola,listbox_cpu,procesos))
    #hilo2=th.Thread(target=show_cpu,args=(listbox_cpu,listbox_cola,procesos))
    hilo1.start()
    #hilo1.join() # esperamos a que termine 
    #hilo2.start()
    #hilo2.join() # esperamos a que termine
    
boton_iniciar = tk.Button(ventana, text="Iniciar Simulación", command=lambda: algoritmo_fcfs(procesos))
boton_iniciar.place(x=350, y=10)

# Iniciar la aplicación
ventana.mainloop()





