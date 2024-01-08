import matplotlib.pyplot as plt
from collections import deque
from log_conf import configurar_logger
import logging

def plot_diagrama_gantt(recorrido: list):  
    
    COLOR = ('red', 'blue', 'green', 'yellow', 'skyblue', 'purple')
    
    fig, ax = plt.subplots()

    for i, (tarea, inicio, duracion) in enumerate(recorrido):
        ax.barh(i, duracion, left=inicio, height=0.5, align='center', label=tarea, color=COLOR[i], edgecolor='black')
    
    ax.set_yticks(range(0, len(recorrido)))
    ax.set_yticklabels([f'{proceso[0]}' for proceso in recorrido])
    ax.grid(True)
    
    plt.xlabel('Tiempo')
    plt.ylabel('Proceso')
    plt.title('Gantt Chart')

    plt.show()
    
def diagrama_gantt_fcfs(procesos: deque):    
    procesos_completados, recorrido = fcfs(procesos)    
    plot_diagrama_gantt(recorrido)
    
def diagrama_gantt_round_robin(procesos: deque, quantum: float):    
    procesos_completados, recorrido = round_robin(procesos, quantum)   
    plot_diagrama_gantt(recorrido)

def diagrama_gantt_round_robin(procesos: deque, quantum: float):    
    procesos_completados, recorrido = round_robin(procesos, quantum)   
    plot_diagrama_gantt(recorrido)

def round_robin(procesos: deque, quantum: float):
    tiempo_actual = 0
    tiempo_transcurrido = 0
    procesos_completados = []
    recorrido = []

    while procesos:
        proceso = procesos.popleft()
        if proceso.obtener_tiempo_restante() > quantum:
            tiempo_transcurrido = quantum
            proceso.establecer_tiempo_restante(proceso.obtener_tiempo_restante() - quantum)
            procesos.append(proceso)

        else:
            tiempo_transcurrido = proceso.obtener_tiempo_restante()
            proceso.establecer_tiempo_restante(0)
            procesos_completados.append((proceso.obtener_nombre(), tiempo_actual))
                  
        recorrido.append((proceso.obtener_nombre(), tiempo_actual, tiempo_transcurrido))
        tiempo_actual += tiempo_transcurrido

    return procesos_completados, recorrido[::-1]

def fcfs(procesos: deque):
    tiempo_actual = 0
    procesos_completados = []
    recorrido = []

    while procesos:
        proceso = procesos.popleft()
         
        if tiempo_actual < proceso.obtener_tiempo_restante():
            recorrido.append((proceso.obtener_nombre(), tiempo_actual, proceso.obtener_tiempo_restante()))
            tiempo_actual = proceso.obtener_tiempo_restante()   
                      
        tiempo_actual += proceso.obtener_rafaga()
        procesos_completados.append((proceso.obtener_nombre(), tiempo_actual))
        
    return procesos_completados, recorrido[::-1]

def sjf(procesos: list):
    
    procesos.sort(key=lambda proceso: (proceso.obtener_tiempo_restante(), proceso.obtener_rafaga()))
    
    tiempo_actual = 0
    procesos_completados = []
    procesos_restantes = list(procesos)
    recorrido = []
    
    while procesos_restantes:
        proceso_elegible = [p for p in procesos_restantes if p.obtener_tiempo_restante() <= tiempo_actual]
        if not proceso_elegible:
            tiempo_actual += 1
            continue
        trabajo_mas_corto = min(proceso_elegible, key=lambda proceso: proceso.obtener_rafaga())
        procesos_restantes.remove(trabajo_mas_corto)
        recorrido.append((trabajo_mas_corto.obtener_nombre(), tiempo_actual, trabajo_mas_corto.obtener_tiempo_restante()))
        tiempo_actual += trabajo_mas_corto.obtener_rafaga()
        procesos_completados.append((trabajo_mas_corto.obtener_nombre(), tiempo_actual))

    return procesos_completados, recorrido