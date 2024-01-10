import tkinter as tk
import time
import logging
import threading as th
import process_info
from DiagramaGantt import plot_diagrama_gantt
from collections import deque
from log_conf import configurar_logger

configurar_logger()   
logger = logging.getLogger('sfj.py')

def mostrar_cola_procesos(listbox: tk.Listbox, procesos: list):
    for proceso in procesos:
        listbox.insert(tk.END, f'Proceso: {proceso.obtener_nombre()} -Rafaga: {proceso.obtener_rafaga()}')
        time.sleep(0.015)
         
def sfj(cola_procesos: tk.Listbox, procesos_comp: tk.Listbox, procesos: deque, grafico_gantt: bool, automatico: bool):  
     
    anterior_tiempo_espera = 0
    anterior_rafaga = 0 
    
    procesos_completados = []
    recorrido = [] 
    
    inicio_recorrido = 0
    final_recorrido = 0 
    
    NUMERO_BARRAS = 6
    primera_iteracion = True
    
    tiempo_respuesta_promedio = 0
    tiempo_espera_promedio = 0
    
    while procesos:             
        proceso = procesos.popleft()  
        
        if primera_iteracion:        
            proceso.establecer_tiempo_respuesta(proceso.obtener_rafaga() + proceso.obtener_tiempo_espera())
            anterior_tiempo_espera = proceso.obtener_tiempo_espera()
            anterior_rafaga = proceso.obtener_rafaga()
            primera_iteracion = False
            recorrido.append((proceso.obtener_nombre(), proceso.obtener_tiempo_espera(), proceso.obtener_rafaga()))
        else:
            proceso.establecer_tiempo_espera(anterior_rafaga + anterior_tiempo_espera) #- proceso.obtener_tiempo_llegada()
            if proceso.obtener_tiempo_espera() < 0:
                proceso.establecer_tiempo_espera(0)
                     
        proceso.establecer_tiempo_respuesta(proceso.obtener_rafaga() + proceso.obtener_tiempo_espera())
           
        procesos_completados.append((proceso.obtener_nombre(), proceso.obtener_tiempo_respuesta()))
        recorrido.append((proceso.obtener_nombre(), proceso.obtener_tiempo_espera(), proceso.obtener_rafaga()))
        
        anterior_tiempo_espera = proceso.obtener_tiempo_espera()
        anterior_rafaga = proceso.obtener_rafaga() 
        
        final_recorrido += 1
        cola_procesos.delete(0) 
        procesos_comp.insert(tk.END,f'Proceso: {proceso.obtener_nombre()} -Tiempo de Finalizacion: {proceso.obtener_tiempo_respuesta()}')
        
        if grafico_gantt and final_recorrido % NUMERO_BARRAS == 0:
            aux_recorrido = recorrido[inicio_recorrido:final_recorrido]
            
            for nombre, inicio, duracion in aux_recorrido:
                logger.info(f'(Recorrido) Nombre: {nombre} Inicio: {inicio} Duracion: {duracion}')
            
            plot_diagrama_gantt(aux_recorrido[::-1])
        
            inicio_recorrido = final_recorrido
                       
    if grafico_gantt and inicio_recorrido != final_recorrido:
        aux_recorrido = recorrido[inicio_recorrido:final_recorrido]
        
        for nombre, inicio, duracion in aux_recorrido:
            logger.info(f'(Recorrido) Nombre: {nombre} Inicio: {inicio} Duracion: {duracion}')
       
        plot_diagrama_gantt(aux_recorrido[::-1])
            
    return procesos_completados, recorrido

def show_multiple(cola_procesos, procesos_completados, procesos, grafico_gantt, automatico):
  
    if procesos_completados.size() > 0:
        procesos_completados.delete(0, tk.END)
    
    mostrar_cola_procesos(cola_procesos, procesos)
    recorrido = sfj(cola_procesos, procesos_completados, deque(procesos), grafico_gantt, automatico)[1]
    
    logger.info(f'Grafico Gantt: {grafico_gantt} Automatico: {automatico}')
    
    if not grafico_gantt:
        for nombre, inicio, duracion in recorrido:
            logger.info(f'(Recorrido) Nombre: {nombre} Inicio: {inicio} Duracion: {duracion}')
    
       
def algoritmo_sfj(procesos: list, grafico_gantt: bool, automatico: bool):
    hilo1=th.Thread(target=show_multiple, args=(listbox_cola, listbox_procesos_completados, procesos, grafico_gantt, automatico))
    hilo1.start()

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
    ventana.title("Simulación SFJ")
    
    procesos = process_info.obtener_procesos_fecha_llegada()
    procesos.sort(key=lambda proceso: proceso.obtener_rafaga())

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
     
    # Variable para almacenar el estado
    grafico_gantt = tk.BooleanVar()
    automatico = tk.BooleanVar()

    # Crear botón de opción
    boton_diagrama_gantt = tk.Checkbutton(ventana, text="Grafico de Gantt", variable=grafico_gantt)
    boton_diagrama_gantt.pack()
    boton_diagrama_gantt.place(x=ANCHO_VENTANA / 2 + ANCHO_BOTON / 2, y=ALTURA_VENTANA - ALTURA_BOTON - 10, width=ANCHO_BOTON, height=ALTURA_BOTON)
    
    boton_iniciar = tk.Button(ventana, text="Iniciar Simulación", command=lambda: algoritmo_sfj(procesos, grafico_gantt.get(), automatico.get()))
    boton_iniciar.place(x=ANCHO_VENTANA / 2 - ANCHO_BOTON - 50, y=ALTURA_VENTANA - ALTURA_BOTON - 10, width=ANCHO_BOTON, height=ALTURA_BOTON)

    # Iniciar la aplicación
    ventana.mainloop()