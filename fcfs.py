import tkinter as tk

class Proceso:
    def __init__(self, id, tiempoLlegada, tiempoRafaga, tiempoEspera=0, tiempoRespuesta=0):
        self.id = id
        self.tiempoLlegada = tiempoLlegada
        self.tiempoRafaga = tiempoRafaga
        self.tiempoEspera = tiempoEspera
        self.tiempoRespuesta = tiempoRespuesta


def initProcess(procesos, n):
    for i in range(n):
        id = i + 1
        # Crear una etiqueta para pedir el numero de procesos
        tiempoLlegada = int(input(f"Tiempo de llegada para el proceso {id}: "))
        tiempoRafaga = int(input(f"Tiempo de rafaga para el proceso {id}: "))
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
    for proceso in procesos:
        print(f"Proceso {proceso.id}, T. llegada {proceso.tiempoLlegada}, "
              f"T. rafaga {proceso.tiempoRafaga}, "
              f"T. espera {proceso.tiempoEspera}, "
              f"T. respuesta {proceso.tiempoRespuesta}.")


#variable para almacenar el numero de procesos
nroProcesos=0

def obteniendoNroProcesos(inputNroProcesos):
    global nroProcesos
    valorNroProcesos=inputNroProcesos.get()

    try:
        # Intenta convertir el valor a un número entero
        nroProcesos = int(valorNroProcesos)
    except ValueError:
        # Si no se puede convertir a número entero, muestra un mensaje de error
        print("El numero ingresado no es un entero")


def main():
    # Crear la ventana principal
    print("inicio")
    ventana = tk.Tk()
    ventana.title("ALGORITMO FCFS")
    ventana.geometry("600x600")
    print("Creando ventana principal")
    # Crear una etiqueta para pedir el numero de procesos
    labelNroProcesos = tk.Label(ventana, text="Ingrese el numero de procesos: ")
    labelNroProcesos.pack(pady=10)
    
    # Crear un campo de entrada (input), para recibir el numero de procesos
    inputNroProcesos = tk.Entry(ventana)
    inputNroProcesos.pack(pady=10)
    
    # Botón para obtener los valores ingresados
    boton = tk.Button(ventana, text="Obteniendo los valores", command=lambda: obteniendoNroProcesos(inputNroProcesos))
    boton.pack(pady=10)
    ventana.mainloop()
    print(nroProcesos)
    if(nroProcesos == 0):
        return
    
    #nroProcesos = int(input("Ingrese el numero de procesos: "))
    procesos = []
    initProcess(procesos, nroProcesos)
    print("INICIO")
    mostrarProcesos(procesos)
    fcfs(procesos)


if __name__ == "__main__":
    main()

