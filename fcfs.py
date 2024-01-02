import tkinter as tk
import subprocess

#Crear la ventana principal
print("inicio")
ventana = tk.Tk()
ventana.title("ALGORITMO FCFS")
ventana.geometry("600x600")
print("Creando ventana principal")

# Nombre del archivo de salida
nombre_archivo = 'salida.txt'
# variable para almacenar el numero de procesos
nroProcesos=0

# Lista de procesos
procesos=[]

#listbox
listbox = tk.Listbox(ventana, width=50, height=10)
listbox.pack(pady=20)

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
        nroProcesos+=1





class Proceso:
    def __init__(self, id, tiempoLlegada, tiempoRafaga, tiempoEspera=0, tiempoRespuesta=0):
        self.id = id
        self.tiempoLlegada = tiempoLlegada
        self.tiempoRafaga = tiempoRafaga
        self.tiempoEspera = tiempoEspera
        self.tiempoRespuesta = tiempoRespuesta


def initProcess():
    #obteniendo el numero de procesos
    
    #mostrando el numero de procesos
    labelNroEtiquetas = tk.Label(ventana, text=f"El numero de procesos actual es: {nroProcesos}")
    labelNroEtiquetas.pack()
    #ventana.mainloop()
    for i in range(nroProcesos):
        id = i + 1
        # Crear una etiqueta para pedir el numero de procesos
        #en esta parte se va a obtener los datos de los procesos del sistema
        tiempoLlegada = 0 #se supone que el tiempo de inicio es 0 para todos los procesos
        tiempoRafaga = 5
        procesos.append(Proceso(id, tiempoLlegada, tiempoRafaga))


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
    mostrarProcesos(procesos)
    print(f"Tiempo de espera promedio: {tiempoEsperaPromedio / n:.2f} milisegundos.")
    print(f"Tiempo de respuesta promedio: {tiempoRespuestaPromedio / n:.2f} milisegundos.")


def fcfs(procesos):
    ordenarProcesosPorTiempoLlegada(procesos)
    print("ORDENADO")
    mostrarProcesos(procesos)
    tiempoEsperaYRespuesta(procesos)


def mostrarProcesos(procesos):
    listbox.delete(0, tk.END)  # Limpiar el Listbox antes de agregar nuevos elementos
    for proceso in procesos:
        """
        print(f"Proceso {proceso.id}, T. llegada {proceso.tiempoLlegada}, "
              f"T. rafaga {proceso.tiempoRafaga}, "
              f"T. espera {proceso.tiempoEspera}, "
              f"T. respuesta {proceso.tiempoRespuesta}.")
        """

        info = (f"Proceso {proceso.id}, T. llegada {proceso.tiempoLlegada}, "
                f"T. rafaga {proceso.tiempoRafaga}, "
                f"T. espera {proceso.tiempoEspera}, "
                f"T. respuesta {proceso.tiempoRespuesta}.")
        listbox.insert(tk.END, info)

        ventana.mainloop()




def main():
    
    # Botón para obtener los valores ingresados
    boton = tk.Button(ventana, text="Obtener los procesos", command=initProcess)
    boton.pack(pady=10)
    ventana.mainloop()
    print(nroProcesos)
    if(nroProcesos == 0):
        return
    
    print("INICIO")
    mostrarProcesos(procesos)
    #fcfs(procesos)


if __name__ == "__main__":
    main()

