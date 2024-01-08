import tkinter as tk

class Proceso:
    def __init__(self, nombre, tiempo_llegada, duracion):
        self.nombre = nombre
        self.tiempo_llegada = tiempo_llegada
        self.duracion = duracion
        self.tiempo_inicio = None
        self.tiempo_finalizacion = None

    def __repr__(self):
        return f"Proceso(nombre='{self.nombre}', tiempo_llegada={self.tiempo_llegada}, duracion={self.duracion})"

# Asegúrate de que el archivo 'procesos.txt' esté en el mismo directorio que este script, o proporciona la ruta completa al archivo.
archivo_procesos = 'valores.txt'

procesos = []

# Abrir el archivo para leer los datos de los procesos
with open(archivo_procesos, 'r') as archivo:
    for linea in archivo:
        # Ignorar líneas vacías
        if linea.strip() == '':
            continue

        try:
            partes = linea.replace("'", "").split('-')
            nombre = partes[0].strip()
            tiempo_llegada = float(partes[1].split(':')[1].strip())
            duracion = int(partes[2].split(':')[1].strip())
            procesos.append(Proceso(nombre, tiempo_llegada, duracion))

        except (IndexError, ValueError) as e:
            print(f"Error procesando la línea: '{linea.strip()}'. Error: {e}")

# Mostrar la lista de procesos
for proceso in procesos:
    print(proceso)
def archivo():
    return procesos
