import tkinter as tk
from tkinter import ttk
from process_info import obtener_info_procesos
from filters import filtro, filtro2
import subprocess

def showfinal(actual):
    actual.delete(0, tk.END)
    datos = filtro2()
    for nombre, tiempo_llegada,tiempo_rafaga in datos:
        actual.insert(tk.END, f"'{nombre}' - Time: '{tiempo_llegada}'-Rafaga:'{tiempo_rafaga}'")
def obtener_valores(listbox):
    try:
        valores = listbox.get(0, tk.END)  # Obtiene todos los valores de la ListBox
        with open('valores.txt', 'w') as f:
            for valor in valores:
                f.write(str(valor) + '\n')
    except Exception as e:
        print(f"Error: {e}")
def run_script():#ejecuta FCFS
    # Ejecuta el script Python en un nuevo proceso
    subprocess.run(["python", "alg_fcfs.py"])
def run_scriptFJS():
    subprocess.run(["python","alfFJS.py"])
def showtotal(actual):
    showfinal(actual)
    obtener_valores(actual)
    run_script()
def showtotalFJS(actual):
    showfinal(actual)
    obtener_valores(actual)
    run_scriptFJS()

def actualizar_datos(tree, ventana):
    for i in tree.get_children():
        tree.delete(i)
    procesos_origin = obtener_info_procesos()
    procesos = filtro(procesos_origin)
    for proceso in procesos:
        tree.insert('', 'end', values=proceso)
    ventana.after(5000, lambda: actualizar_datos(tree, ventana))

def valores_actual():
    vec=[]
    for val in actual.size():
        vec.append(actual.get(val))
    return vec

def create_gui():
    ventana = tk.Tk()
    ventana.geometry("800x600")
    ventana.title("Información de Procesos")
    # (Aquí iría el resto de la configuración de la GUI, treeview, labels, botones, etc.)
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
    tree.column('PID', width=60, minwidth=5)
    tree.column('Nombre', width=100, minwidth=50)
    tree.column('Usuario', width=100, minwidth=50)
    tree.column('Memoria', width=80, minwidth=40)
    tree.column('Timellegada', width=100, minwidth=50)#tiempo que demora el proceso para llegar al sistema
    tree.column('Timeejecucion', width=100, minwidth=50)
    tree.column('Timerafaga', width=100, minwidth=50)

    #dimensiones del treeview
    tree.place(x=0, y=0, width=600, height=400)
    #nuevos colas de procesos//////////////////////////////////
    label = tk.Label(ventana,text="Procesos en Cola")
    label.place(x=605,y=0,width=150,height=20)#inicia en la esquina superior de y=0)
    #BOX
    cola_pro = tk.Listbox(ventana, width=20, height=10)
    cola_pro.insert(2, "Opción 2 en Listbox 1")
    cola_pro.place(x=605,y=20,width=200,height=100)
    #Procesos en el CPU////////////////////////////////////////////
    labelcpu = tk.Label(ventana,text="Procesos en el cpu")
    labelcpu.place(x=605,y=125,width=150,height=20)
    #BOX
    cpu_pro = tk.Listbox(ventana, width=20, height=10)  # 20 caracteres de ancho, 10 líneas de alto
    cpu_pro.insert(1, "Opción 1 en Listbox 1")
    cpu_pro.insert(2, "Opción 2 en Listbox 1")
    cpu_pro.place(x=605,y=150,width=200,height=100)
    #PROCEOS ACTUAL ?///////////////////////
    labelactual = tk.Label(ventana,text="Proceso Actual")
    labelactual.place(x=605,y=255,width=150,height=20)
    #BOX
    actual = tk.Listbox(ventana, width=20, height=10)  # 20 caracteres de ancho, 10 líneas de alto
    actual.place(x=605,y=275,width=200,height=100)
      
    # Botón para actualizar manualmente
    boton_actualizar = tk.Button(ventana, text="Actualizar", command=lambda: actualizar_datos(tree, ventana))
    boton_actualizar.pack()
    boton_actualizar.place(x=0, y=410, width=70, height=25)
    # ...
    # BOTON FCFS
    boton_fcfs = tk.Button(ventana, text='FCFS', command=lambda: showtotal(actual))
    boton_fcfs.pack()
    boton_fcfs.place(x=80, y=410, width=70, height=25)
    #BOTON CALCULAR   
    #boton_calcular =tk.Button(ventana,text='ejecucion',command=run_script)
    #boton_calcular.pack()
    #boton_calcular.place(x=80, y=435, width=70, height=25)
    #BOTON_FJS 
    boton_fjs = tk.Button(ventana, text='FJS', command=lambda: showtotalFJS(actual))
    boton_fjs.pack()
    boton_fjs.place(x=160, y=410, width=70, height=25)
    # Iniciar la actualización automática
    actualizar_datos(tree, ventana)
    ventana.mainloop()

    return create_gui


