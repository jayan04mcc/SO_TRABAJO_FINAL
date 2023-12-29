import psutil
import tkinter as tk
from tkinter import ttk
import datetime
import time
import random
def obtener_info_procesos():
    # Lista para mantener la información de los procesos
    procesos = []
    for pid in psutil.pids():
        try:
            p = psutil.Process(pid)
            # Obtén la información deseada
            pid = p.pid
            nombre = p.name()
            usuario = p.username()
            memoria = p.memory_info().rss  # memoria en uso
            tiempo_llegada=random.randint(1,5)
            tiempo_creacion = p.create_time()
            tiempo_ejecucion = time.time() - tiempo_creacion  #Tiempo que toma para
                                                                 #completar su proceso en la CPU , similara al tiempo de rafaga
            tiempo_ejecucion=round(tiempo_ejecucion,2)
            # Obtiene el tiempo de CPU antes de la ejecución
            tiempo_cpu_antes = p.cpu_times()

            # Obtiene el tiempo de CPU después de la ejecución
            tiempo_cpu_despues = p.cpu_times()

            # Calcula el tiempo de ráfaga como la diferencia en el tiempo de CPU
            tiempo_rafaga = tiempo_cpu_despues.user - tiempo_cpu_antes.user
                                   
            
            procesos.append((pid, nombre, usuario, memoria,tiempo_llegada, tiempo_ejecucion,tiempo_rafaga))

        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue
    return procesos
def filtro(resul):
    final=[]
    for elem in resul:
        if 'kali' in elem and elem[5]<1000:
            final.append(elem)
    return final

# Función para actualizar los datos mostrados
def actualizar_datos():
    # Eliminar los datos existentes
    for i in tree.get_children():
        tree.delete(i)
    # Obtener los nuevos datos de los procesos
    
    procesos_origin = obtener_info_procesos()
    procesos = filtro(procesos_origin)

    # Añadir nuevos datos al Treeview
    for proceso in procesos:
        tree.insert('', 'end', values=proceso)

    # Programar la siguiente actualización
    ventana.after(5000, actualizar_datos)  # actualizar cada 5 segundos

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Información de Procesos")

# Crear el Treeview
tree = ttk.Treeview(ventana, columns=('PID', 'Nombre', 'Usuario', 'Memoria','Timellegada','Timeejecucion','Timerafaga'), show='headings')
tree.heading('PID', text='PID')
tree.heading('Nombre', text='Nombre')
tree.heading('Usuario', text='Usuario')
tree.heading('Memoria', text='Memoria (bytes)')
tree.heading('Timellegada',text='Time llegada')
tree.heading('Timeejecucion',text='Time ejecucion')
tree.heading('Timerafaga',text='Time rafaga')

tree.pack(expand=True, fill='both')


# Botón para actualizar manualmente
boton_actualizar = tk.Button(ventana, text="Actualizar Ahora", command=actualizar_datos)
boton_actualizar.pack()

# Iniciar la actualización automática
actualizar_datos()

# Ejecutar la aplicación
ventana.mainloop()
