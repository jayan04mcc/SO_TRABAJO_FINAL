from collections import deque

class Proceso:
    def __init__(self, nombre, tiempo_llegada, duracion):
        self.nombre = nombre
        self.tiempo_llegada = tiempo_llegada
        self.duracion = duracion
        self.tiempo_inicio = None
        self.tiempo_finalizacion = None

def FCFS(procesos):
    procesos.sort(key=lambda x: x.tiempo_llegada)
    cola = deque(procesos)
    tiempo_actual = 0
    procesos_en_cpu = []

    while cola or procesos_en_cpu:
        # Actualizar la cola de procesos
        while cola and cola[0].tiempo_llegada <= tiempo_actual:
            procesos_en_cpu.append(cola.popleft())

        if procesos_en_cpu:
            proceso_actual = procesos_en_cpu.pop(0)
            tiempo_actual = max(tiempo_actual, proceso_actual.tiempo_llegada) + proceso_actual.duracion
            proceso_actual.tiempo_finalizacion = tiempo_actual

        # Devuelve el estado actual de la cola y la CPU
        yield cola, procesos_en_cpu
