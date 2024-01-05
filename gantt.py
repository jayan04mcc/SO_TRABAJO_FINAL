import matplotlib.pyplot as plt
import numpy as np
from fcfs import procesos, inicio, duracion

from matplotlib.backend_bases import Event


#clases para interactuar con el mouse
from matplotlib.backend_bases import MouseEvent




#funcion para manejar el evento de la rueda del mouse
def on_scroll(event):
    #se llama a una funcion que al inicio ocultara los numeros del eje y
    #por cuestion estetica cuando haya muchos procesos
    on_ylims_change(event)
    # Definir factor de escala
    scale_factor = 1.2
    
    # Verificar dirección del scroll
    if event.step < 0:
        # Scroll hacia abajo (zoom out)
        scale_factor = 1 / scale_factor
    
    # Aplicar zoom a la gráfica
    ax = event.inaxes
    if ax is not None:
        xdata = event.xdata  # posición x del mouse en coordenadas de datos
        ydata = event.ydata  # posición y del mouse en coordenadas de datos

        # Ajustar los límites de los ejes basándonos en la posición del mouse
        ax.set_xlim([xdata - (xdata - ax.get_xlim()[0]) * scale_factor,
                     xdata + (ax.get_xlim()[1] - xdata) * scale_factor])
        ax.set_ylim([ydata - (ydata - ax.get_ylim()[0]) * scale_factor,
                     ydata + (ax.get_ylim()[1] - ydata) * scale_factor])
    
        plt.draw()



nroProcesos=len(procesos)

#creando un arreglo para obtener los nombres
#de los procesos
maquinas=[]
for i in range(nroProcesos):
   maquinas.append(procesos[i].id)

# Datos
ht = 20 #numero de tiempo que se vera en un inicio
nmaq = nroProcesos #numero de procesos
hbar = 20 #altura de cada barra
tticks = 10 #no se usa
#maquinas = ["P1", "P2", "P3","P4","P5"] #nombres de las maquinas

# Creación de los objetos del plot:
fig, gantt = plt.subplots()

# Etiquetas de los ejes:
gantt.set_xlabel("Tiempo")
gantt.set_ylabel("Procesos")

# Límites de los ejes:
gantt.set_xlim(0, ht)
gantt.set_ylim(0, nmaq*hbar)

# Divisiones del eje de tiempo:
gantt.set_xticks(range(0, ht, 1), minor=True)
gantt.grid(True, axis='x', which='both')

# Divisiones del eje de máquinas:
gantt.set_yticks(range(hbar, nmaq*hbar, hbar), minor=True)
gantt.grid(True, axis='y', which='minor')

# Etiquetas de máquinas:
gantt.set_yticks(np.arange(hbar/2, hbar*nmaq - hbar/2 + hbar, hbar))


#gantt.set_yticklabels(maquinas)

# Función para armar tareas:
def agregar_tarea(t0, d, maq, nombre, color):
# Índice de la máquina:
    imaq = maquinas.index(maq)
    # Posición de la barra:
    gantt.broken_barh([(t0, d)], (hbar*imaq, hbar),
                        facecolors=(color))
    #Posición del texto:
    #gantt.text(x=(t0 + d/2), y=(hbar*imaq + hbar/2),
     #              s=f"{nombre} ({d})", va='center', color='white')

# Agregamos dos tareas de ejemplo:

#agregar_tarea(0, 9, "P1", "T1", "b")

#agregamos tareas
for i in range(nroProcesos):
    agregar_tarea(inicio[i],duracion[i],maquinas[i],"xd","m")


# Guarda la imagen en la ruta especificada
ruta_imagen = "static/img/gantt.svg"
fig.savefig(ruta_imagen)


# Oculta las etiquetas del eje Y
gantt.set_yticklabels([])

#elimina los numeros del eje y
gantt.set_yticklabels([])


# Función para mostrar etiquetas cuando se hace zoom en el eje Y
def on_ylims_change(event: Event):
    if event.name == 'scroll_event':
        if event.inaxes == gantt:
            gantt.set_yticklabels(maquinas)
        else:
            gantt.set_yticklabels([])


#conectar la funcion de la rueda del mouse
fig.canvas.mpl_connect('scroll_event', on_scroll)


plt.show()
# Cierra la figura para liberar memoria
plt.close(fig)

