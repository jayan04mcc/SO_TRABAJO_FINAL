import matplotlib.pyplot as plt
import logging
from log_conf import configurar_logger

configurar_logger()   
logger = logging.getLogger('DiagramaGantt.py')

def graficar_recorrido():
     
    recorrido = []
    final_recorrido = 0 
    
    NUMERO_BARRAS = 6
    
    with open('recorrido.txt', 'r') as archivo:      
        for linea in archivo:
            if linea.strip() == '':
                continue          
            try:          
                valores = linea.split()
                recorrido.append((valores[0], float(valores[1]), float(valores[2])))
                logger.info(f'graficar_recorrido: {valores}')
            except IndexError as e:
                logger.error(e)
            except ValueError as e:
                logger.error(e)
     
    while True: 
        if final_recorrido + NUMERO_BARRAS < len(recorrido):      
            aux_recorrido = recorrido[final_recorrido:final_recorrido+NUMERO_BARRAS]        
            plot_diagrama_gantt(aux_recorrido[::-1])  
            final_recorrido += NUMERO_BARRAS
        else:
            aux_recorrido = recorrido[final_recorrido:len(recorrido)] 
            plot_diagrama_gantt(aux_recorrido[::-1])  
            break
        
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
    
    plt.pause(3)
    plt.close()    
    plt.show()
    
if __name__ == "__main__":
    graficar_recorrido()