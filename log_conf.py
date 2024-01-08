import logging

def configurar_logger():
    logging.basicConfig(filename='app.log', filemode='w', level=logging.DEBUG,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
