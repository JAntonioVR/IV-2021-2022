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


    def buscar_resenias_por_local(self, local):
        ''' Método que devuelve todas las reseñas de un local dado.
        
        Argumentos:
        arg1 (string): Local del que se quieren buscar reseñas.
        '''
        result = []
        for resenia in self.resenias:
            if(resenia.local_id == local):
                result.append(result)
        return result

    def buscar_resenia_por_indice(self, index):
        return self.resenias[index]

    def carga_datos(self, dataset):
        self.resenias = []
        with open(dataset) as csvfile:
            spamreader = csv.reader(csvfile, delimiter='\t')
            for row in spamreader:
                current_review = resenia.Resenia(row[0], row[3], row[2], None)
                self.resenias.append(current_review)

        self.resenias.pop(0) # La primera reseña eran los nombres de las columnas

    def numero_resenias(self):
        return len(self.resenias)
