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
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Crear la ventana principal
ventana = tk.Tk()
ventana.geometry("800x600")
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
#definimos las columnas
tree.column('PID', width=20, minwidth=5)
tree.column('Nombre', width=100, minwidth=50)
tree.column('Usuario', width=100, minwidth=50)
tree.column('Memoria', width=80, minwidth=40)
tree.column('Timellegada', width=100, minwidth=50)
tree.column('Timeejecucion', width=100, minwidth=50)
tree.column('Timerafaga', width=100, minwidth=50)

#dimensiones del treeview
tree.place(x=0, y=0, width=600, height=400)



# Botón para actualizar manualmente
boton_actualizar = tk.Button(ventana, text="Actualizar", command=actualizar_datos)
boton_actualizar.pack()
boton_actualizar.place(x=0,y=410,width=70,height=25)
#nuevos colas de procesos
label = tk.Label(ventana,text="Procesos en Cola")
label.place(x=605,y=0,width=150,height=20)
Cola_pro = tk.Listbox(ventana, width=20, height=10)  # 20 caracteres de ancho, 10 líneas de alto
Cola_pro.insert(2, "Opción 2 en Listbox 1")
Cola_pro.place(x=605,y=20,width=200,height=100)
#Procesos en el CPu

labelcpu = tk.Label(ventana,text="Procesos en el cpu")
labelcpu.place(x=605,y=125,width=150,height=20)
cpu_pro = tk.Listbox(ventana, width=20, height=10)  # 20 caracteres de ancho, 10 líneas de alto
cpu_pro.insert(1, "Opción 1 en Listbox 1")
cpu_pro.insert(2, "Opción 2 en Listbox 1")
cpu_pro.place(x=605,y=150,width=200,height=100)
# Iniciar la actualización automática
actualizar_datos()
# Ejecutar la aplicación
ventana.mainloop()
