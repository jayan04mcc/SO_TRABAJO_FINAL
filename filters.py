from process_info import obtener_info_procesos

def filtro(resul):
    final = []
    for elem in resul:
        if 'kali' in elem and elem[4] < 1000:
            final.append(elem)
    return final

def filtro2():
    todos_los_procesos = obtener_info_procesos()
    data_final = filtro(todos_los_procesos)
    nombre_tiempo_llegada = [(proceso[1], proceso[4],proceso[6]) for proceso in data_final]
    return nombre_tiempo_llegada

