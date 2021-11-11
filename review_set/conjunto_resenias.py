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
                        current_review = resenia.Resenia(row[0], row[3], int(row[2]), None)
                        self.resenias.append(current_review)
                except UnicodeDecodeError:
                    print("Error: No se ha podido abrir el fichero " + dataset)
            

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
        '''Método que devuelve el número de reseñas del conjunto
        '''
        return len(self.resenias)
