import psutil
import time
import random

def obtener_info_procesos():
    # Lista para mantener la información de los procesos
    procesos = []
    for pid in psutil.pids():
        try:
            p = psutil.Process(pid)
            # Obtén la información deseada
            pid = p.pid
            nombre = p.name()
            usuario = p.username()
            memoria = p.memory_info().rss  # memoria en uso
            
            tiempo_ejecucion = random.randint(1, 5) # varia entre 10 y 1000 milisegundos
            tiempo_creacion = p.create_time()
            tiempo_llegada = time.time() - tiempo_creacion
            #tiempo_llegada=p.create_time()
            tiempo_llegada = round(tiempo_llegada, 2)
            tiempo_rafaga = random.randint(1,5) #tiempo que necesita para ejecutarse en la cpu sin interrupciones
                                                #sistema batch y tiempo compartido
            procesos.append((pid, nombre, usuario, memoria, tiempo_llegada, tiempo_ejecucion, tiempo_rafaga))
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue
    return procesos

