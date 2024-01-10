import tkinter as tk
import time
import logging
import threading as th
import process_info
from collections import deque
from log_conf import configurar_logger
from DiagramaGantt import plot_diagrama_gantt

configurar_logger()   
logger = logging.getLogger('round_robin.py')

def mostrar_cola_procesos(listbox: tk.Listbox, procesos: list):
    for proceso in procesos:
        listbox.insert(tk.END, f'Proceso: {proceso.obtener_nombre()} -Rafaga: {proceso.obtener_rafaga()}')
        time.sleep(0.015)
    
def round_robin(cola_procesos: tk.Listbox, procesos_comp: tk.Listbox, procesos: deque, quantum: float, diagrama_gantt: bool):  
    tiempo_actual = 0
    inicio_proceso = 0
    tiempo_transcurrido = 0
    procesos_completados = []
    recorrido = []  
    inicio_recorrido = 0
    final_recorrido = 0   
    NUMERO_BARRAS = 6
     
    while procesos:
        proceso = procesos.popleft()    
          
        if proceso.obtener_tiempo_restante() > quantum:
            tiempo_actual += quantum
            tiempo_transcurrido = quantum
            proceso.establecer_tiempo_restante(proceso.obtener_tiempo_restante() - quantum)
            procesos.append(proceso)
            cola_procesos.delete(0)   
            cola_procesos.insert(tk.END, f'Proceso: {proceso.obtener_nombre()} -Rafaga: {proceso.obtener_tiempo_restante()}')
        else:
            tiempo_actual += proceso.obtener_tiempo_restante()
            tiempo_transcurrido = proceso.obtener_tiempo_restante()

            proceso.establecer_tiempo_espera(tiempo_actual - tiempo_transcurrido)
            proceso.establecer_tiempo_respuesta(tiempo_transcurrido + proceso.obtener_tiempo_espera())
            proceso.establecer_tiempo_restante(0)
            
            procesos_completados.append((proceso.obtener_nombre(), proceso.obtener_tiempo_respuesta()))
            cola_procesos.delete(0) 
            procesos_comp.insert(tk.END,f'Proceso: {proceso.obtener_nombre()} -Tiempo de Finalizacion: {tiempo_actual}')
       
        recorrido.append((proceso.obtener_nombre(), inicio_proceso, tiempo_transcurrido))
        inicio_proceso += tiempo_transcurrido
        final_recorrido += 1 
  
        if diagrama_gantt and final_recorrido % NUMERO_BARRAS == 0:
            aux_recorrido = recorrido[inicio_recorrido:final_recorrido]
            
            for nombre, inicio, duracion in aux_recorrido:
                logger.info(f'(Recorrido) Nombre: {nombre} Inicio: {inicio} Duracion: {duracion}')
            
            plot_diagrama_gantt(aux_recorrido[::-1])
        
            inicio_recorrido = final_recorrido
                       
    if diagrama_gantt and inicio_recorrido != final_recorrido:
        aux_recorrido = recorrido[inicio_recorrido:final_recorrido]
        
        for nombre, inicio, duracion in aux_recorrido:
            logger.info(f'(Recorrido) Nombre: {nombre} Inicio: {inicio} Duracion: {duracion}')
       
        plot_diagrama_gantt(aux_recorrido[::-1])
    
    return procesos_completados, recorrido

def show_multiple(cola_procesos, procesos_completados, procesos, quantum: float, diagrama_gantt: bool):
    
    if procesos_completados.size() > 0:
        procesos_completados.delete(0, tk.END)
    
    mostrar_cola_procesos(cola_procesos, procesos)
    recorrido = round_robin(cola_procesos, procesos_completados, deque(procesos), quantum, diagrama_gantt)[1]
    
    logger.info(f'Grafico Gantt: {diagrama_gantt}')
    
    if not diagrama_gantt:
        for nombre, inicio, duracion in recorrido:
            logger.info(f'(Recorrido) Nombre: {nombre} Inicio: {inicio} Duracion: {duracion}')

def algoritmo_round_robin(procesos: list, quantum: float, diagrama_gantt: bool):
    logger.info(f'Quantum: {quantum}')
    hilo1=th.Thread(target=show_multiple, args=(listbox_cola, listbox_procesos_completados, procesos, quantum, diagrama_gantt))
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
    ventana.title("Simulación Round Robin")
    procesos = process_info.obtener_procesos_fecha_llegada()

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
    diagrama_gantt = tk.BooleanVar()
        
    titulo_entrada_quantum = tk.Label(ventana, text="Quantum: ")
    titulo_entrada_quantum.pack()
    titulo_entrada_quantum.place(x=ANCHO_VENTANA / 2, y=ALTURA_VENTANA - ALTURA_BOTON - 10, width=ANCHO_BOTON, height=ALTURA_BOTON)
    entrada_quantum  = tk.Entry(ventana)
    entrada_quantum .pack()
    entrada_quantum .place(x=ANCHO_VENTANA / 2 + 100, y=ALTURA_VENTANA - ALTURA_BOTON - 10, width=ANCHO_BOTON / 2, height=ALTURA_BOTON)
    
    # Crear botón de opción
    boton_diagrama_gantt = tk.Checkbutton(ventana, text="Grafico de Gantt", variable=diagrama_gantt)
    boton_diagrama_gantt.pack()
    boton_diagrama_gantt.place(x=ANCHO_VENTANA / 2 + ANCHO_BOTON, y=ALTURA_VENTANA - ALTURA_BOTON - 10, width=ANCHO_BOTON, height=ALTURA_BOTON)
            
    boton_iniciar = tk.Button(ventana, text="Iniciar Simulación", command=lambda: algoritmo_round_robin(procesos, float(entrada_quantum.get()), diagrama_gantt.get()))
    boton_iniciar.place(x=ANCHO_VENTANA / 2 - ANCHO_BOTON - 50, y=ALTURA_VENTANA - ALTURA_BOTON - 10, width=ANCHO_BOTON, height=ALTURA_BOTON)

    ventana.mainloop()