import psutil
import time

def obtener_procesos():
    # Crear una lista vacía para almacenar los procesos
    procesos = []

    # Iterar sobre todos los PIDs en el sistema
    for pid in psutil.pids():
        try:
            proceso = psutil.Process(pid)
            nombre = proceso.name()
            
            # Obtener el tiempo de creación del proceso y calcular el tiempo de llegada
            tiempo_creacion = proceso.create_time()
            tiempo_llegada = round(time.time() - tiempo_creacion,3)
            
            # Obtener el tiempo total de ejecución (tiempo de ráfaga) del proceso
            tiempo_rafaga = round(sum(proceso.cpu_times()),3)
            
            procesos.append((pid, nombre, tiempo_llegada, tiempo_rafaga))
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue

    return procesos

# Obtener la lista de procesos
#lista_procesos = obtener_procesos()
lista_procesos=[["p1","p2","p3","p4","p5"],["Word","Excel","VSCode","Google","Paint"],[0,0,0,0,0],[10,1,2,1,5]]



