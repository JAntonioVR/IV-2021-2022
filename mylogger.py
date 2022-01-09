# Fichero de logging, que controla y encapsula todo lo relacionado con el logging de la aplicación

import logging
from configuracion import Configuracion

# ─── NIVELES DE LOGGING ─────────────────────────────────────────────────────────
levels = {
    'DEBUG': logging.DEBUG,
    'INFO': logging.INFO,
    'WARNING': logging.WARNING,
    'ERROR': logging.ERROR,
    'CRITICAL': logging.CRITICAL
}


# ─── MYLOGGER ───────────────────────────────────────────────────────────────────

class MyLogger:
    ''' Clase que utiliza la biblioteca logging y que actua como interfaz de logging
    
    Atributos:
    file (str): Ruta del fichero de logging.
    level (int): Constante que indica el nivel de logging
    logger (logging.RootLogger): Logger que utiliza la biblioteca para hacer todo
                                 el tratamiento de los logs.
    '''
    def __init__(self):
        configuracion = Configuracion()
        self.file = configuracion.get_logging_path()
        self.level = configuracion.get_logging_level()
        self.format = configuracion.get_logging_format()
        logging.basicConfig(filename = self.file,
                            filemode = "w",
                            format = self.format, 
                            level = self.level)
        
        self.logger = logging.getLogger()

    # ─── FUNCIONES DE REGISTRO DE EVENTOS ───────────────────────────────────────────
    # Actúan como interfaz de la biblioteca logging.

    def debug(self, msg):
        self.logger.debug(msg)
    
    def info(self, msg):
        self.logger.info(msg)
    
    def warning(self, msg):
        self.logger.warning(msg)
    
    def error(self, msg):
        self.logger.error(msg)
    
    def critical(self, msg):
        self.logger.critical(msg)

# ────────────────────────────────────────────────────────────────────────────────
