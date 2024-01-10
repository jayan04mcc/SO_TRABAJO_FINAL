import tkinter as tk
import subprocess
import logging
import process_info
from log_conf import configurar_logger
from tkinter import ttk
from platform import system

configurar_logger()
logger = logging.getLogger('gui.py')

def run_script_python(direccion: str):
    subprocess.run(["python", direccion])

def show_fcfs():
    run_script_python('fcfs.py')

def show_sfj():
    run_script_python('sfj.py')

def show_round_robin():
    run_script_python('round_robin.py')

def actualizar_datos(tree: ttk.Treeview, vista_primer_plano: tk.Listbox, vista_segundo_plano: tk.Listbox, ventana: tk.Tk):
    
    for valor in tree.get_children():
        tree.delete(valor)
    vista_primer_plano.delete(0, tk.END)
    vista_segundo_plano.delete(0, tk.END)
    
    procesos = process_info.obtener_todos_los_procesos()
    procesos_primer_plano = process_info.obtener_procesos_primer_plano()
    procesos_segundo_plano = process_info.obtener_procesos_segundo_plano()
    
    for proceso in procesos:
        tree.insert('', 'end', values=(proceso.obtener_pid(), proceso.obtener_nombre(), proceso.obtener_usuario(), proceso.obtener_rafaga(), proceso.obtener_fecha_llegada().strftime('%Y-%m-%d %H:%M:%S')))
    
    for proceso in procesos_primer_plano:
        vista_primer_plano.insert(tk.END, f'Pid: {proceso.obtener_pid()} -Nombre: {proceso.obtener_nombre()}')
        
    for proceso in procesos_segundo_plano:
        vista_segundo_plano.insert(tk.END, f'Pid: {proceso.obtener_pid()} -Nombre: {proceso.obtener_nombre()}')
    
    ventana.after(5000, lambda: actualizar_datos(tree, vista_primer_plano, vista_segundo_plano, ventana))
    logger.info('actualizar_datos(): Procesos Actualizados')

def create_gui():
    
    ANCHO_PANTALLA = 900
    ALTURA_PANTALLA = 650

    ANCHO_VISTAS = 280
    ALTURA_VISTAS = 220
    ANCHO_TITULOS = ANCHO_VISTAS
    ALTURA_TITULOS = 20
     
    ANCHO_BOTON = ANCHO_VISTAS
    ALTURA_BOTON = 35
    
    ANCHO_VISTA_PROCESOS = 600
    ALTURA_VISTA_PROCESOS = ALTURA_VISTAS * 2 + ALTURA_TITULOS * 3 + ALTURA_BOTON * 3
    
    # Crear la ventana principal
    ventana = tk.Tk()
    ventana.geometry(f'{ANCHO_PANTALLA}x{ALTURA_PANTALLA}')
    ventana.title(f'Información de Procesos en {system()}')

    #Titulo Lista de Procesos
    inicial = tk.Label(ventana,text="Procesos Actuales")
    inicial.place(x=0, y=0, width=ANCHO_VISTA_PROCESOS, height=ALTURA_TITULOS)
    
    # Crear el Treeview
    tree = ttk.Treeview(ventana, columns=('PID', 'Nombre', 'Usuario','Tiempo de rafaga', 'Fecha de Llegada'), show='headings')
    tree.heading('PID', text='PID')
    tree.heading('Nombre', text='Nombre')
    tree.heading('Usuario', text='Usuario')
    tree.heading('Tiempo de rafaga',text='Tiempo de rafaga (s)')
    tree.heading('Fecha de Llegada',text='Fecha de Llegada')
    #Definimos las columnas
    tree.column('PID', width=20, minwidth=5)
    tree.column('Nombre', width=100, minwidth=50)
    tree.column('Usuario', width=100, minwidth=50)
    tree.column('Tiempo de rafaga', width=100, minwidth=50)
    tree.column('Fecha de Llegada', width=80, minwidth=40)
    #Dimensiones del treeview
    tree.place(x=0, y=ALTURA_TITULOS, width=ANCHO_VISTA_PROCESOS, height=ALTURA_VISTA_PROCESOS)
    
    #Titulo Procesos Primer Plano
    titulo_primer_plano = tk.Label(ventana,text="Procesos Primer Plano")
    titulo_primer_plano.place(x=605, y=0, width=ANCHO_TITULOS, height=ALTURA_TITULOS)
    vista_primer_plano = tk.Listbox(ventana, width=20, height=10) 
    vista_primer_plano.place(x=605, y=ALTURA_TITULOS, width=ANCHO_VISTAS, height=ALTURA_VISTAS)
    
    #Titulo Procesos Segundo Plano
    titulo_segundo_plano = tk.Label(ventana,text="Procesos Segundo Plano")
    titulo_segundo_plano.place(x=605, y=ALTURA_VISTAS, width=ANCHO_TITULOS, height=ALTURA_TITULOS)
    vista_segundo_plano = tk.Listbox(ventana, width=20, height=10)  # 20 caracteres de ancho, 10 líneas de alto
    vista_segundo_plano.place(x=605, y=ALTURA_TITULOS + ALTURA_VISTAS, width=ANCHO_VISTAS, height=ALTURA_VISTAS)
    
    #Algoritmos
    algoritmos = tk.Label(ventana,text="Simular Ejecucion")
    algoritmos.place(x=605, y=ALTURA_TITULOS * 2 + ALTURA_VISTAS * 2, width=ANCHO_TITULOS, height=ALTURA_TITULOS)                
    #BOTON FCFS
    boton_fcfs =tk.Button(ventana, text='FCFS', command=lambda: show_fcfs())
    boton_fcfs.pack()
    boton_fcfs.place(x=605, y=ALTURA_TITULOS * 2 + ALTURA_VISTAS * 2 + ALTURA_BOTON, width=ANCHO_BOTON, height=ALTURA_BOTON)
    #BOTON SJC
    boton_sjc =tk.Button(ventana, text='SJF', command=lambda: show_sfj())
    boton_sjc.pack()
    boton_sjc.place(x=605, y=ALTURA_TITULOS * 2 + ALTURA_VISTAS * 2 + ALTURA_BOTON * 2, width=ANCHO_BOTON, height=ALTURA_BOTON)
    #BOTON RR
    boton_round_robin =tk.Button(ventana, text='Round Robin', command=lambda: show_round_robin())
    boton_round_robin.pack()
    boton_round_robin.place(x=605, y=ALTURA_TITULOS * 2 + ALTURA_VISTAS * 2 + ALTURA_BOTON * 3, width=ANCHO_BOTON, height=ALTURA_BOTON)
    
    # Iniciar la actualización automática
    actualizar_datos(tree, vista_primer_plano, vista_segundo_plano, ventana)
    ventana.mainloop()