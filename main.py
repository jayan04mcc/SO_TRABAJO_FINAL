import tkinter as tk
import Proceso
import logging
import DiagramaGantt
from platform import system
from collections import deque
from log_conf import configurar_logger
from tkinter import ttk

def filtro(resul):
    final=[]
    for elem in resul:
        if 'kali' in elem and elem[5]<1000:
            final.append(elem)
    return final

 #Función para actualizar los datos mostrados
def actualizar_datos(tree: ttk.Treeview, ventana: tk.Tk):
    # Eliminar los datos existentes
    for i in tree.get_children():
        tree.delete(i)
    # Obtener los nuevos datos de los procesos
    
    procesos = Proceso.obtener_procesos()

    # Añadir nuevos datos al Treeview
    for proceso in procesos:
        tree.insert('', 'end', values=(proceso.obtener_pid(), proceso.obtener_nombre(), proceso.obtener_rafaga(), proceso.obtener_tiempo_llegada().strftime("%Y-%m-%d %H:%M:%S")))

    # Programar la siguiente actualización
    #ventana.after(5000, actualizar_datos(tree, ventana))  # actualizar cada 5 segundos

def show_final(actual: tk.Listbox):
    # Limpiar el Listbox
    actual.delete(0, tk.END)
    # Obtener los datos de los procesos   
    procesos = Proceso.obtener_procesos()
    # Insertar los nuevos datos en el Listbox
    for proceso in procesos:
        actual.insert(tk.END, f"{proceso.obtener_nombre()} - Llegada: {proceso.obtener_tiempo_llegada().strftime('%Y-%m-%d %H:%M:%S')}")

def gui_principal():
    # Crear la ventana principal
    ventana = tk.Tk()
    ventana.geometry("800x600")
    ventana.title("Información de Procesos")

    # Crear el Treeview
    tree = ttk.Treeview(ventana, columns=('PID', 'Nombre', 'Tiempo de rafaga', 'Tiempo de llegada'), show='headings')
    tree.heading('PID', text='PID')
    tree.heading('Nombre', text='Nombre')
    tree.heading('Tiempo de rafaga',text='Tiempo de rafaga')
    tree.heading('Tiempo de llegada',text='Tiempo de llegada')

    #definimos las columnas
    tree.column('PID', width=20, minwidth=5)
    tree.column('Nombre', width=100, minwidth=50)
    tree.column('Tiempo de rafaga', width=100, minwidth=50)
    tree.column('Tiempo de llegada', width=80, minwidth=40)

    #dimensiones del treeview
    tree.place(x=0, y=0, width=600, height=400)

    #Botón para actualizar manualmente
    boton_actualizar = tk.Button(ventana, text="Actualizar", command=actualizar_datos(tree, ventana))
    boton_actualizar.pack()
    boton_actualizar.place(x=0,y=410,width=70,height=25)

    #nuevos colas de procesos
    label = tk.Label(ventana,text="Procesos en Cola")
    label.place(x=605,y=0,width=150,height=20)#inicia en la esquina superior de y=0)
    #BOX
    cola_pro = tk.Listbox(ventana, width=20, height=10) 
    cola_pro.insert(2, "Opción 2 en Listbox 1")
    cola_pro.place(x=605,y=20,width=200,height=100)
    #Procesos en el CPU
    labelcpu = tk.Label(ventana,text="Procesos en el cpu")
    labelcpu.place(x=605,y=125,width=150,height=20)
    #BOX
    cpu_pro = tk.Listbox(ventana, width=20, height=10)  # 20 caracteres de ancho, 10 líneas de alto
    cpu_pro.insert(1, "Opción 1 en Listbox 1")
    cpu_pro.insert(2, "Opción 2 en Listbox 1")
    cpu_pro.place(x=605,y=150,width=200,height=100)
    #PROCEOS ACTUAL
    labelactual = tk.Label(ventana,text="Proceso Actual")
    labelactual.place(x=605,y=255,width=150,height=20)
    #BOX
    actual = tk.Listbox(ventana, width=20, height=10)  # 20 caracteres de ancho, 10 líneas de alto
    actual.insert(1, "Opción 1 en Listbox 1")
    actual.insert(2, "Opción 2 en Listbox 1")
    actual.place(x=605,y=275,width=200,height=100)

    #BOTON FCFS
    boton_fcfs =tk.Button(ventana, text='FCFS',command=show_final(actual))
    boton_fcfs.pack()
    boton_fcfs.place(x=80,y=410,width=70,height=25)

    # Iniciar la actualización automática
    #actualizar_datos(tree, ventana)
    # Ejecutar la aplicación
    ventana.mainloop()
    
if __name__ == '__main__':
    
    configurar_logger()   
    logger = logging.getLogger('main.py')
    logger.info(f"Sistema Operativo: {system()}")