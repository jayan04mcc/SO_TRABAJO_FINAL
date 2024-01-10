import logging
from platform import system
from gui import create_gui
from log_conf import configurar_logger
from getpass import getuser

if __name__ == "__main__":   
    configurar_logger()   
    logger = logging.getLogger('main.py')
    logger.info(f"Sistema Operativo: {system()}")
    logger.info(f"Usuario: {getuser()}")
    create_gui()