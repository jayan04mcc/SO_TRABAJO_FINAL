#2DO ARCHIVO
#se extrae los procesos obtenidos del sistema, los cuales se encuentran en la lista_procesos
from x import lista_procesos

respuestas=[]
#listas para realizar los graficos
inicio=[]
duracion=[]

class Proceso:
    def __init__(self, id, nombre, tiempoLlegada, tiempoRafaga, tiempoEspera=0, tiempoRespuesta=0):
        self.id = id
        self.tiempoLlegada = tiempoLlegada
        self.tiempoRafaga = tiempoRafaga
        self.nombre=nombre
        self.tiempoEspera = tiempoEspera
        self.tiempoRespuesta = tiempoRespuesta


def initProcess():
    procesos=[]
    for i in range(len(lista_procesos)):
        tiempoLlegada=lista_procesos[i][2]
        tiempoRafaga=lista_procesos[i][3]
        procesos.append(Proceso(lista_procesos[i][0], lista_procesos[i][1], tiempoLlegada, tiempoRafaga))
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
        tiempoEspera = round(clock - proceso.tiempoLlegada,3)
        proceso.tiempoEspera = tiempoEspera
        tiempoEsperaPromedio += tiempoEspera

        tiempoRespuesta = round(tiempoEspera + proceso.tiempoRafaga,3)
        proceso.tiempoRespuesta = tiempoRespuesta
        tiempoRespuestaPromedio += tiempoRespuesta
        #guardando la informacion necesaria para realizar el grafico
        inicio.append(clock)
        duracion.append(proceso.tiempoRafaga)

        clock += proceso.tiempoRafaga

    #print("COMPLETO")
    #print(f"Tiempo de espera promedio: {tiempoEsperaPromedio / n:.2f} milisegundos.")
    #print(f"Tiempo de respuesta promedio: {tiempoRespuestaPromedio / n:.2f} milisegundos.")
    respuestas.append(round(tiempoEsperaPromedio/n,3))
    respuestas.append(round(tiempoRespuestaPromedio/n,3))

def mostrarProcesos(procesos):
    for proceso in procesos:
        
        print(f"Proceso {proceso.id}, T. llegada {proceso.tiempoLlegada}, "
              f"T. rafaga {proceso.tiempoRafaga}, "
              f"T. espera {proceso.tiempoEspera}, "
              f"T. respuesta {proceso.tiempoRespuesta}.")
        

def fcfs(procesos):
    ordenarProcesosPorTiempoLlegada(procesos)
    tiempoEsperaYRespuesta(procesos)


# Lista de procesos
procesos=initProcess()
fcfs(procesos)



