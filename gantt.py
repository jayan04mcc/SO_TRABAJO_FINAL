import matplotlib.pyplot as plt
import numpy as np
from fcfs import procesos, inicio, duracion

nroProcesos=len(procesos)

#creando un arreglo para obtener los nombres
#de los procesos
maquinas=[]
for i in range(nroProcesos):
   maquinas.append(procesos[i].id)

# Datos
ht = 50 #ancho_total
nmaq = 5 #numero de procesos
hbar = 10 #altura de cada barra
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


gantt.set_yticklabels(maquinas)

# Función para armar tareas:
def agregar_tarea(t0, d, maq, nombre, color):
# Índice de la máquina:
    imaq = maquinas.index(maq)
    # Posición de la barra:
    gantt.broken_barh([(t0, d)], (hbar*imaq, hbar),
                        facecolors=(color))
    # Posición del texto:
    #gantt.text(x=(t0 + d/2), y=(hbar*imaq + hbar/2),
     #               s=f"{nombre} ({d})", va='center', color='white')

# Agregamos dos tareas de ejemplo:

#agregar_tarea(0, 9, "P1", "T1", "b")

#agregamos tareas
for i in range(5):
    agregar_tarea(inicio[i],duracion[i],maquinas[i],"xd","m")


# Guarda la imagen en la ruta especificada
ruta_imagen = "static/img/gantt.svg"
fig.savefig(ruta_imagen)

# Cierra la figura para liberar memoria
plt.close(fig)

#plt.show()
