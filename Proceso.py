import psutil
import datetime
import logging
from random import randint
from time import time
from log_conf import configurar_logger

configurar_logger()   
logger = logging.getLogger('Proceso.py')

class Proceso:
    _nombre = ""
    _pid = -1
    _tiempo_llegada = None
    _rafaga = 0
    _tiempo_restante = 0

    def __init__(self, pid: int, nombre: str, rafaga: float, tiempo_llegada: datetime.datetime):
        self._nombre = nombre
        self._tiempo_llegada = tiempo_llegada
        self._rafaga = rafaga
        self._pid = pid
        self._tiempo_restante = rafaga
    
    def __str__ (self):
        return f"Pid: {self._pid} \tNombre: {self._nombre}\tRafaga: {self._rafaga}\tTiempo de llegada: {self._tiempo_llegada.strftime('%Y-%m-%d %H:%M:%S')}"
    
    def obtener_tiempo_llegada(self):
        return self._tiempo_llegada
    
    def obtener_nombre(self):
        return self._nombre
    
    def obtener_pid(self):
        return self._pid
    
    def obtener_rafaga(self):
        return self._rafaga
    
    def obtener_tiempo_restante(self):
        return self._tiempo_restante
    
    def establecer_tiempo_restante(self, tiempo_restante: float):
        self._tiempo_restante = tiempo_restante
    
def obtener_procesos():
    lista_procesos = psutil.process_iter()
    procesos = []
    n = 0
    for proceso in lista_procesos:
        try:
            # Obtener informacion detallada del proceso
            info_proceso = proceso.as_dict(attrs=['name', 'pid', 'cpu_times', 'create_time'])

            # Obtener el tiempo de rafaga de CPU en segundos
            tiempo_rafaga_usuario = info_proceso['cpu_times'].user
            tiempo_rafaga_sistema = info_proceso['cpu_times'].system
            
            # Obtener fecha en que empezo a ejecutarse
            tiempo_inicio = datetime.datetime.fromtimestamp(info_proceso['create_time'])

            procesos.append(Proceso(info_proceso['pid'], info_proceso['name'], tiempo_rafaga_usuario + tiempo_rafaga_sistema, tiempo_inicio))
            logger.info(f"obtener_procesos(): {procesos[n]}")
            n += 1
            
        except psutil.NoSuchProcess as e:
            logger.error(e.msg)
            
    procesos.sort(key=lambda proceso: proceso.obtener_tiempo_llegada())
    
    return procesos[3:]