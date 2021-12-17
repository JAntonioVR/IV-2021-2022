import logging
from configuracion import Configuracion
from review_set.conjunto_resenias import ConjuntoResenias
import sys

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
        self.logger.info(msg)
    
    def warning(self, msg):
        self.logger.warning(msg)
    
    def error(self, msg):
        self.logger.error(msg)
    
    def critical(self, msg):
        self.logger.critical(msg)


class ConjuntoReseniasFactory:
    def __init__(self, dataset = None):
        self.logger = MyLogger()
        self.logger.debug("Creando de una instancia de ConjuntoResenia")
        self.conjunto_resenias = ConjuntoResenias(dataset)
        if self.conjunto_resenias == None:
            self.logger.critical("No se ha creado correctamente el objeto ConjuntoResenia.")
            sys.exit(-1)
        elif self.conjunto_resenias.numero_resenias() == 0:
            self.logger.info("Se ha creado un conjunto de reseñas vacío.")

    def buscar_resenias_por_local(self, local_id : str):
        self.logger.debug("Buscando reseñas de " + local_id)
        resenias_local = self.conjunto_resenias.buscar_resenias_por_local(local_id)
        n_resenias = resenias_local.numero_resenias()
        if n_resenias == 0:
            self.logger.info("No se han encontrado reseñas de " + local_id)
        else:
            self.logger.info("Se han encontrado " + str(n_resenias) + " reseñas de " + local_id)
    
    def buscar_resenia_por_indice(self, index: int):
        self.logger.debug("Buscando la reseña de índice " + str(index))
        resenia = None
        try:
            resenia = self.conjunto_resenias.buscar_resenia_por_indice(index)
        except IndexError:
            self.logger.error("No se ha encontrado la reseña de índice " + str(index))
        return resenia

    def numero_resenias(self):
        ''' Método que devuelve el número de reseñas del conjunto
        '''
        return self.conjunto_resenias.numero_resenias()
   