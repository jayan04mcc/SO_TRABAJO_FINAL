import tkinter as tk
import time
from collections import deque
from queue import Queue
import threading as th
import tests as te
ejecuciones =0
cont_cpu=1
ventana = tk.Tk()
ventana.geometry("800x400")
ventana.title("Simulación FCFS")
procesos = te.archivo()
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
        for elemento in elementos:
            listbox.insert(tk.END, f"{elemento.nombre} -Llegada: {elemento.tiempo_llegada}")
            time.sleep(1)
        # Incrementar el contador de ejecuciones
        ejecuciones += 1

def show_cpu(listbox,listbox2,elementos):#cpu cola
    global cont_cpu
    while cont_cpu<=len(elementos):
        listbox.insert(tk.END,f"{elementos[cont_cpu-1].nombre} -TimeEjec: {elementos[cont_cpu-1].duracion}")# trabajamos con la listbox cpu
        for i in range(elementos[cont_cpu-1].duracion):
            listbox.insert(tk.END,f"{i+1}...")
            time.sleep(0.5)
        time.sleep(1)
        listbox.delete(0, tk.END)
        if listbox2.size()>0:
            listbox2.delete(0)
            time.sleep(1)
        cont_cpu += 1
def show_multiple(cola,cpu,elementos):
    show(cola, elementos)
    show_cpu(cpu,cola, elementos)

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





