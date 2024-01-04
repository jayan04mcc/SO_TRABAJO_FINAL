import tkinter as tk
from x import lista_procesos



class Proceso:
    def __init__(self, id, tiempoLlegada, tiempoRafaga, tiempoEspera=0, tiempoRespuesta=0):
        self.id = id
        self.tiempoLlegada = tiempoLlegada
        self.tiempoRafaga = tiempoRafaga
        self.tiempoEspera = tiempoEspera
        self.tiempoRespuesta = tiempoRespuesta


def initProcess():
    procesos=[]
    for i in range(5):
        tiempoLlegada=lista_procesos[i][2]
        tiempoRafaga=lista_procesos[i][3]
        procesos.append(Proceso(lista_procesos[i][0], tiempoLlegada, tiempoRafaga))
    return procesos

def swap(procesos, i, j):
    procesos[i], procesos[j] = procesos[j], procesos[i]


def ordenarProcesosPorTiempoLlegada(procesos):
    n = len(procesos)
    for i in range(n):
        for j in range(n):
            if procesos[i].tiempoLlegada < procesos[j].tiempoLlegada:
                swap(procesos, i, j)


def tiempoEsperaYRespuesta(procesos):
    n = len(procesos)
    tiempoEsperaPromedio = 0.0
    tiempoRespuestaPromedio = 0.0
    clock = 0.0
    procesos[0].tiempoEspera = clock

    for proceso in procesos:
        tiempoEspera = clock - proceso.tiempoLlegada
        proceso.tiempoEspera = tiempoEspera
        tiempoEsperaPromedio += tiempoEspera

        tiempoRespuesta = tiempoEspera + proceso.tiempoRafaga
        proceso.tiempoRespuesta = tiempoRespuesta
        tiempoRespuestaPromedio += tiempoRespuesta

        clock += proceso.tiempoRafaga

    print("COMPLETO")
    print(f"Tiempo de espera promedio: {tiempoEsperaPromedio / n:.2f} milisegundos.")
    print(f"Tiempo de respuesta promedio: {tiempoRespuestaPromedio / n:.2f} milisegundos.")

def mostrarProcesos(procesos):
    for proceso in procesos:
        
        print(f"Proceso {proceso.id}, T. llegada {proceso.tiempoLlegada}, "
              f"T. rafaga {proceso.tiempoRafaga}, "
              f"T. espera {proceso.tiempoEspera}, "
              f"T. respuesta {proceso.tiempoRespuesta}.")
        

def fcfs(procesos):
    ordenarProcesosPorTiempoLlegada(procesos)
    #print("ORDENADO")
    #mostrarProcesos(procesos)
    tiempoEsperaYRespuesta(procesos)
    #print("Finalizo")




# Lista de procesos
procesos=initProcess()
fcfs(procesos)



