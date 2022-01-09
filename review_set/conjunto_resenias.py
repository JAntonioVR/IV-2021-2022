# Fichero de la clase ConjuntoResenias, clase que modela y controla el conjunto de todas las reseñas

from dataclasses import dataclass
from typing import List

from review_set.resenia import Resenia
import csv
import sys
from mylogging import MyLogger

@dataclass
class ConjuntoResenias:
    '''Clase para almacenar un conjunto de reseñas.
    
    Atributos:
    resenias (List[Resenia]): Conjunto de reseñas almacenado.
    '''

    resenias: List[Resenia]

    def __init__(self, dataset = None):
        '''Constructor: carga en el atributo 'resenias' una lista de objetos
        de la clase 'Resenia' a partir de un fichero de texto.

        Argumentos:
        arg1 (string): Ruta del fichero del cual se leerán los datos
        '''
        self.resenias = []
        if(dataset!=None):
            with open(dataset) as csvfile:
                try:
                    spamreader = csv.reader(csvfile, delimiter='\t')
                    next(spamreader)        # La primera línea son los nombres de las columnas
                    for row in spamreader:
                        current_review = Resenia(row[0], row[3], int(row[2]), None)
                        self.resenias.append(current_review)
                except UnicodeDecodeError:
                    pass
            
    def buscar_resenias_por_local(self, local_id : str):
        ''' Método que devuelve todas las reseñas de un local dado.
        
        Argumentos:
        arg1 (string): Local del que se quieren buscar reseñas.
        '''
        result = []
        for resenia in self.resenias:
            if(resenia.local_id == local_id):
                result.append(resenia)
        conjunto = ConjuntoResenias()
        conjunto.resenias = result
        return conjunto

    def buscar_resenia_por_indice(self, index: int):
        ''' Método que devuelve la reseña que ocupa el lugar 'index'
        en la lista de reseñas

        Argumentos:
        arg1 (int): Índice de la reseña que se busca
        '''
        return self.resenias[index]

    def numero_resenias(self):
        ''' Método que devuelve el número de reseñas del conjunto
        '''
        return len(self.resenias)



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
