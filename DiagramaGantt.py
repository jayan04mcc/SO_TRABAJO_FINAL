import matplotlib.pyplot as plt

def plot_diagrama_gantt(recorrido: list):  

    fig, ax = plt.subplots()
    
    for i, (tarea, inicio, duracion) in enumerate(recorrido):
        ax.barh(i, duracion, left=inicio, height=0.5, align='center', label=tarea, color='red', edgecolor='black')
    
    ax.set_yticks(range(0, len(recorrido)))
    ax.set_yticklabels([f'{proceso[0]}' for proceso in recorrido])
    ax.grid(True)
    
    plt.xlabel('Tiempo')
    plt.ylabel('Proceso')
    plt.title('Gantt Chart')
    
    plt.show()