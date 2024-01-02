import threading
import time

def tarea_larga():
    print("Iniciando tarea larga...")
    time.sleep(5)  # Simula una tarea que tarda 5 segundos
    print("Tarea larga completada.")

def tarea_corta():
    print("Iniciando tarea corta...")
    time.sleep(2)  # Simula una tarea que tarda 2 segundos
    print("Tarea corta completada.")

# Crea los hilos
hilo_largo = threading.Thread(target=tarea_larga)
hilo_corto = threading.Thread(target=tarea_corta)

# Inicia el hilo largo
hilo_largo.start()

# Espera a que el hilo largo termine
hilo_largo.join()

# Ahora que el hilo largo ha terminado, inicia el hilo corto
hilo_corto.start()

# Espera a que el hilo corto termine
hilo_corto.join()

print("Ambos hilos han terminado.")
