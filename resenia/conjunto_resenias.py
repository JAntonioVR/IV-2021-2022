# Fichero de la clase ConjuntoResenias, clase que modela y controla el conjunto de todas las reseñas

from dataclasses import dataclass
from typing import List

import resenia

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
        pass
