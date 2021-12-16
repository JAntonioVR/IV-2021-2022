import logging
from configuracion import Configuracion

levels = {
    'DEBUG': logging.DEBUG,
    'INFO': logging.INFO,
    'WARNING': logging.WARNING,
    'ERROR': logging.ERROR,
    'CRITICAL': logging.CRITICAL
}

class MyLogger:
    def __init__(self):
        configuracion = Configuracion()
        self.file = configuracion.get_logging_file()
        self.level = configuracion.get_logging_level()
        format = "%(levelname)s :  %(asctime)s - %(message)s"   # FIXME Parametrizo el formato???

        logging.basicConfig(filename = self.file,
                            filemode = "w",
                            format = format, 
                            level = self.level)
        
        self.logger = logging.getLogger()

    def debug(self, msg):
        self.logger.debug(msg)
    
    def info(self, msg):
        self.logger.debug(msg)
    
    def warning(self, msg):
        self.logger.warning(msg)
    
    def error(self, msg):
        self.logger.error(msg)
    
    def critical(self, msg):
        self.logger.critical(msg)
