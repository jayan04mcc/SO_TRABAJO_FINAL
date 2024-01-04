import subprocess
import tkinter as tk

# Nombre del archivo de salida
nombre_archivo = 'salida.txt'

# Ejecutar un comando y redirigir la salida a un archivo de texto
with open(nombre_archivo, 'w') as archivo:
    subprocess.run('ps -eo pid,comm,%cpu,%mem --sort=-%cpu | head', shell=True, stdout=archivo, text=True)

print(f"La salida del comando se ha guardado en {nombre_archivo}")

with open(nombre_archivo, 'r') as archivo_entrada:
    # Lee todas las líneas del archivo
    lineas = archivo_entrada.readlines()

# Elimina los espacios en blanco al inicio de cada línea y sobrescribe el archivo original
with open(nombre_archivo, 'w') as archivo_salida:
    for linea in lineas:
        linea_sin_espacios = linea.lstrip()  # Elimina espacios en blanco al inicio
        archivo_salida.write(linea_sin_espacios)

tercera_columna = []
lista_total=[]
# Lee el contenido del archivo modificado
with open(nombre_archivo, 'r') as archivo_modificado:
    for linea in archivo_modificado:
        if not linea.strip():
            continue  # Ignorar líneas vacías

        palabras = linea.split()  # Ajustar según el delimitador correcto
        if len(palabras) >= 3:
            tercera_columna.append(palabras[2].strip())
        lista_total.append(palabras)

misProcesos={"VSCode","Python", "Java", "PHP", "C++", "Google Chrome"}
