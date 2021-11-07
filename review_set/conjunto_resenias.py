# Fichero de la clase ConjuntoResenias, clase que modela y controla el conjunto de todas las reseñas

from dataclasses import dataclass
from typing import List

import resenia
import csv
import os

@dataclass
class ConjuntoResenias:
    '''Clase para almacenar un conjunto de reseñas.
    
    Atributos:
    resenias (List[resenia.Resenia]): Conjunto de reseñas almacenado.
    '''

    resenias: List[resenia.Resenia]


    def buscar_resenias_por_local(self, local_id : str):
        ''' Método que devuelve todas las reseñas de un local dado.
        
        Argumentos:
        arg1 (string): Local del que se quieren buscar reseñas.
        '''
        result = []
        for resenia in self.resenias:
            if(resenia.local_id == local_id):
                result.append(resenia)
        return ConjuntoResenias(result)

    def buscar_resenia_por_indice(self, index: int):
        ''' Método que devuelve la reseña que ocupa el lugar 'index'
        en la lista de reseñas

        Argumentos:
        arg1 (int): Índice de la reseña que se busca
        '''
        return self.resenias[index]

    def carga_datos(self, dataset: str):
        '''Método que carga en el atributo 'resenias' una lista de objetos
        de la clase 'Resenia' a partir de un fichero de texto.

        Argumentos:
        arg1 (string): Ruta del fichero del cual se leerán los datos
        '''
        self.resenias = []
        with open(dataset) as csvfile:
            spamreader = csv.reader(csvfile, delimiter='\t')
            assert(spamreader != None)
            next(spamreader)        # La primera línea son los nombres de las columnas
            for row in spamreader:
                current_review = resenia.Resenia(row[0], row[3], int(row[2]), None)
                self.resenias.append(current_review)


    def numero_resenias(self):
        '''Método que devuelve el número de reseñas del conjunto
        '''
        return len(self.resenias)
