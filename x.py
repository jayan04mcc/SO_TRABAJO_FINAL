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
lista_procesos=[
    ("p1","Word",0,10),
    ("p2","Excel",0,1),
    ("p3","VSCode",0,2),
    ("p4","Python",0,1),
    ("p5","Google",0,5),
]



