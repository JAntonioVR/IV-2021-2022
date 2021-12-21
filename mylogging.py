# Fichero de logging, que controla y encapsula todo lo relacionado con el logging de la aplicación

import logging
from configuracion import Configuracion
from review_set.conjunto_resenias import ConjuntoResenias
import sys

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


# ─── CONJUNTORESENIASFACTORY ────────────────────────────────────────────────────

class ConjuntoReseniasFactory:
    ''' Es un wrapper de la clase ConjuntoResenias del módulo 
    review_set.conjunto_resenias, por ello, tiene los mismos métodos que
    aceptan los mismos argumentos y el mismo retorno, pero además utiliza un
    objeto de la clase MyLogger para registrar los eventos.

    Atributos:
    logger (MyLogger): Objeto de la clase MyLogger que interactúa con la biblioteca
                       logging para registrar los eventos.
    conjunto_resenias (ConjuntoResenias): Objeto de la clase ConjuntoResenia sobre
                                          el cual actúa esta clase como wrapper.
    
    '''
    def __init__(self, dataset = None):
        ''' Constructor: Inicializa el logger y el conjunto de reseñas, registrando
        los posibles eventos

        Argumentos:
        arg1 (string): Ruta del fichero del cual se leerán los datos
        '''
        self.logger = MyLogger()
        self.logger.debug("Creando de una instancia de ConjuntoResenia")
        self.conjunto_resenias = ConjuntoResenias(dataset)
        if self.conjunto_resenias == None:
            self.logger.critical("No se ha creado correctamente el objeto ConjuntoResenia.")
            sys.exit(-1)
        elif self.conjunto_resenias.numero_resenias() == 0:
            self.logger.info("Se ha creado un conjunto de reseñas vacío.")

    def buscar_resenias_por_local(self, local_id : str):
        ''' Método que devuelve todas las reseñas de un local dado.
        
        Argumentos:
        arg1 (string): Local del que se quieren buscar reseñas.
        '''
        self.logger.debug("Buscando reseñas de " + local_id)
        resenias_local = self.conjunto_resenias.buscar_resenias_por_local(local_id)
        n_resenias = resenias_local.numero_resenias()
        if n_resenias == 0:
            self.logger.info("No se han encontrado reseñas de " + local_id)
        else:
            self.logger.info("Se han encontrado " + str(n_resenias) + " reseñas de " + local_id)
    
    def buscar_resenia_por_indice(self, index: int):
        ''' Método que devuelve la reseña que ocupa el lugar 'index'
        en la lista de reseñas

        Argumentos:
        arg1 (int): Índice de la reseña que se busca
        '''
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
   
# ────────────────────────────────────────────────────────────────────────────────
