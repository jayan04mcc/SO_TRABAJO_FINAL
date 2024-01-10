import psutil
import datetime
import logging
from log_conf import configurar_logger

configurar_logger()   
logger = logging.getLogger('process_info.py')

class Proceso:
    _nombre = ""
    _pid = -1
    _tiempo_llegada = 0.0
    _rafaga = 0
    _usuario = 0
    _tiempo_restante = 0
    _tiempo_respuesta = 0
    _tiempo_espera = 0
    _fecha_llegada = None

    def __init__(self, pid: int, nombre: str, rafaga: float, usuario: str, fecha_llegada: datetime.datetime):
        self._nombre = nombre
        self._fecha_llegada = fecha_llegada
        self._rafaga = rafaga
        self._pid = pid
        self._usuario = usuario
        self._tiempo_restante = rafaga
        self._tiempo_llegada = (datetime.datetime.now() - fecha_llegada).total_seconds()
    
    def __str__ (self):
        return f"Pid: {self._pid} \tNombre: {self._nombre}\tRafaga: {self._rafaga}\tTiempo de llegada: {self._tiempo_llegada}"
    
    def obtener_tiempo_llegada(self):
        return self._tiempo_llegada
    
    def obtener_nombre(self):
        return self._nombre
    
    def obtener_pid(self):
        return self._pid
    
    def obtener_rafaga(self):
        return self._rafaga
    
    def obtener_usuario(self):
        return self._usuario
    
    def obtener_tiempo_restante(self):
        return self._tiempo_restante
    
    def obtener_tiempo_espera(self):
        return self._tiempo_espera
    
    def obtener_tiempo_respuesta(self):
        return self._tiempo_respuesta
    
    def obtener_fecha_llegada(self):
        return self._fecha_llegada
    
    def establecer_tiempo_restante(self, tiempo_restante: float):
        self._tiempo_restante = tiempo_restante
    
    def establecer_tiempo_espera(self, tiempo_espera: float):
        self._tiempo_espera = tiempo_espera
    
    def establecer_tiempo_respuesta(self, tiempo_respuesta: float):
        self._tiempo_respuesta = tiempo_respuesta
    
    def establecer_tiempo_llegada(self, tiempo_llegada: float):
        self._tiempo_llegada = tiempo_llegada
    
def obtener_todos_los_procesos():
    lista_procesos = psutil.process_iter()
    procesos = []
    n = 0
    for proceso in lista_procesos:
        try:
            # Obtener informacion detallada del proceso
            info_proceso = proceso.as_dict(attrs=['name', 'pid', 'username', 'cpu_times', 'create_time'])
         
            # Obtener el tiempo de rafaga de CPU en segundos
            tiempo_rafaga_usuario = info_proceso['cpu_times'].user
            tiempo_rafaga_sistema = info_proceso['cpu_times'].system
            
            # Obtener fecha en que empezo a ejecutarse
            fecha_llegada = datetime.datetime.fromtimestamp(info_proceso['create_time'])

            procesos.append(Proceso(info_proceso['pid'], info_proceso['name'], tiempo_rafaga_usuario + tiempo_rafaga_sistema, info_proceso['username'], fecha_llegada))
            logger.info(f"obtener_procesos(): {procesos[n]}")
            n += 1
            
        except psutil.NoSuchProcess as e:
            logger.error(e.msg)

    return procesos

def obtener_procesos():

    todos_los_procesos = obtener_todos_los_procesos()
    procesos = []
                 
    for proceso in todos_los_procesos:
        usuario = proceso.obtener_usuario()
        if usuario == "NT AUTHORITY\SYSTEM":
            continue
        procesos.append(proceso)
    return procesos

def obtener_procesos_primer_plano():
    procesos = obtener_procesos() 
    primer_plano = []

    for proceso in procesos:
        usuario = proceso.obtener_usuario()
        if usuario == 'SYSTEM' or usuario == 'root' or usuario is None:
            continue
        primer_plano.append(proceso)
    return primer_plano

def obtener_procesos_segundo_plano():
    procesos = obtener_procesos() 
    segundo_plano = []

    for proceso in procesos:
        usuario = proceso.obtener_usuario()
        if usuario == 'SYSTEM' or usuario == 'root' or usuario is None:
            segundo_plano.append(proceso)
            
    return segundo_plano

def obtener_procesos_fecha_llegada():
    procesos = obtener_procesos() 
    procesos.sort(key=lambda proceso: proceso.obtener_fecha_llegada())
    
    for i in range(len(procesos)):
        procesos[i].establecer_tiempo_llegada(i)
        
    return procesos