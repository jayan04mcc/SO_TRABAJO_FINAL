import tkinter as tk
import time
import logging
import threading as th
import process_info
from collections import deque
from log_conf import configurar_logger
from gui import run_script_python
from tkinter import messagebox

configurar_logger()   
logger = logging.getLogger('fcfs.py')

def mostrar_cola_procesos(listbox: tk.Listbox, procesos: list):
    for proceso in procesos:
        listbox.insert(tk.END, f'Proceso: {proceso.obtener_nombre()} -Rafaga: {proceso.obtener_rafaga()}')
        time.sleep(0.015)
         
def fcfs(cola_procesos: tk.Listbox, procesos_comp: tk.Listbox, procesos: deque):  
    anterior_tiempo_espera = 0
    anterior_rafaga = 0 
   
    procesos_completados = []
    
    recorrido = [] 
    primera_iteracion = True
    
    tiempo_espera_total = 0
    tiempo_respuesta_total = 0
    cantidad_procesos = len(procesos)
        
    if procesos_comp.size() > 0:
        procesos_comp.delete(0, tk.END)
    
    while procesos:             
        proceso = procesos.popleft()  
        
        if primera_iteracion:
            anterior_tiempo_espera = 0
            anterior_rafaga = proceso.obtener_rafaga()
            recorrido.append((proceso.obtener_nombre(), 0, proceso.obtener_rafaga()))
            primera_iteracion = False
            cola_procesos.delete(0) 
            procesos_comp.insert(tk.END,f'Proceso: {proceso.obtener_nombre()} -Tiempo de Finalizacion: {proceso.obtener_rafaga()}')       
            tiempo_espera_total += proceso.obtener_tiempo_espera()
            tiempo_respuesta_total += proceso.obtener_tiempo_respuesta()
            continue
               
        proceso.establecer_tiempo_espera(anterior_tiempo_espera + anterior_rafaga)     
        proceso.establecer_tiempo_respuesta(proceso.obtener_tiempo_espera() + proceso.obtener_rafaga())
           
        recorrido.append((proceso.obtener_nombre(), proceso.obtener_tiempo_espera(), proceso.obtener_rafaga()))
        procesos_completados.append((proceso.obtener_nombre(), proceso.obtener_tiempo_respuesta()))
        
        anterior_tiempo_espera = proceso.obtener_tiempo_espera()
        anterior_rafaga = proceso.obtener_rafaga()
        proceso.establecer_tiempo_restante(0)
        
        cola_procesos.delete(0) 
        procesos_comp.insert(tk.END,f'Proceso: {proceso.obtener_nombre()} -Tiempo de Finalizacion: {proceso.obtener_tiempo_respuesta()}')
        tiempo_espera_total += proceso.obtener_tiempo_espera()
        tiempo_respuesta_total += proceso.obtener_tiempo_respuesta()
    
    return procesos_completados, tiempo_espera_total / cantidad_procesos, tiempo_respuesta_total / cantidad_procesos, recorrido

def show_multiple(cola_procesos, procesos_completados, iteraciones: int):   
    procesos_com= []
    recorrido = []
    tiempo_espera_promedio = 0
    tiempo_respuesta_promedio = 0
    
    for i in range(iteraciones):
        if procesos_completados.size() > 0:
            procesos_completados.delete(0, tk.END)    
        logger.info(f'Iteracion: {i}')      
        procesos = process_info.obtener_procesos_fecha_llegada()
        mostrar_cola_procesos(cola_procesos, procesos)
        aux_procesos_com, aux_tiempo_espera_promedio, aux_tiempo_respuesta_promedio, aux_recorrido = fcfs(cola_procesos, procesos_completados, deque(procesos))
        tiempo_espera_promedio += aux_tiempo_espera_promedio
        tiempo_respuesta_promedio += aux_tiempo_respuesta_promedio
        recorrido.extend(aux_recorrido)
        
    messagebox.showinfo("Resultados", f'Tiempo Espera Promedio: {round(tiempo_espera_promedio / iteraciones, 2)}\nTiempo Respuesta Promedio: {round(tiempo_respuesta_promedio / iteraciones, 2)}')   
    
    try:
        with open('recorrido.txt', 'w') as archivo:
            for nombre, inicio, duracion in recorrido:
                logger.info(f'(Recorrido) Nombre: {nombre} Inicio: {inicio} Duracion: {duracion}')
                archivo.write(f'{nombre} {inicio} {duracion}\n')           
    except Exception as e:
        logger.error(e)
          
def algoritmo_fcfs(iteraciones: int):
    hilo1=th.Thread(target=show_multiple, args=(listbox_cola, listbox_procesos_completados, iteraciones))
    hilo1.start()
    
def grafica_gantt():
    run_script_python('DiagramaGantt.py')

if __name__ == "__main__":   
    
    ANCHO_VENTANA = 800
    ALTURA_VENTANA = 400
    
    ANCHO_VISTAS = 330
    ALTURA_VISTAS = 300
    
    ANCHO_TITULOS = ANCHO_VISTAS
    ALTURA_TITULOS = 20

    ANCHO_BOTON = 150
    ALTURA_BOTON = 30

    ventana = tk.Tk()
    ventana.geometry(f'{ANCHO_VENTANA}x{ALTURA_VENTANA}')
    ventana.title("Simulación FCFS")

    # Crear el Listbox para la cola de procesos
    cola_procesos = tk.Label(ventana, text="Cola de Procesos")
    cola_procesos.place(x=20, y=50 - ALTURA_TITULOS, width=ANCHO_VISTAS, height=ALTURA_TITULOS)
    listbox_cola = tk.Listbox(ventana)
    listbox_cola.place(x=20, y=50, width=ANCHO_VISTAS, height=ALTURA_VISTAS)

    # Crear el Listbox para la CPU
    procesos_compl = tk.Label(ventana, text="Procesos Completados")
    procesos_compl.place(x=450, y=50 - ALTURA_TITULOS, width=ANCHO_VISTAS, height=ALTURA_TITULOS)
    listbox_procesos_completados = tk.Listbox(ventana)
    listbox_procesos_completados.place(x=450, y=50, width=ANCHO_VISTAS, height=ALTURA_VISTAS)
     
    titulo_entrada_iteraciones = tk.Label(ventana, text="Iteraciones: ")
    titulo_entrada_iteraciones.pack()
    titulo_entrada_iteraciones.place(x=ANCHO_VENTANA / 2 - ANCHO_TITULOS - 90, y=ALTURA_VENTANA - ALTURA_BOTON - 10, width=ANCHO_BOTON, height=ALTURA_BOTON)
    entrada_iteraciones  = tk.Entry(ventana)
    entrada_iteraciones.pack()
    entrada_iteraciones.place(x=ANCHO_VENTANA / 2 - ANCHO_TITULOS + 20, y=ALTURA_VENTANA - ALTURA_BOTON - 10, width=ANCHO_BOTON / 2, height=ALTURA_BOTON)

    boton_iniciar = tk.Button(ventana, text="Iniciar Simulación", command=lambda: algoritmo_fcfs(int(entrada_iteraciones.get())))
    boton_iniciar.place(x=ANCHO_VENTANA / 2 - ANCHO_BOTON - 50, y=ALTURA_VENTANA - ALTURA_BOTON - 10, width=ANCHO_BOTON, height=ALTURA_BOTON)

    boton_grafica_gantt = tk.Button(ventana, text="Grafica de Gantt", command=lambda: grafica_gantt())
    boton_grafica_gantt.pack()
    boton_grafica_gantt.place(x=ANCHO_VENTANA / 2 + ANCHO_BOTON / 2 - 25, y=ALTURA_VENTANA - ALTURA_BOTON - 10, width=ANCHO_BOTON, height=ALTURA_BOTON)
    
    # Iniciar la aplicación
    ventana.mainloop()