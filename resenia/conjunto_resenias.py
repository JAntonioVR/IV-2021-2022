# Fichero de la clase ConjuntoResenias, que modela y controla el conjunto de todas las reseñas

from dataclasses import dataclass
from typing import List

import resenia

@dataclass
class ConjuntoResenias:

    resenias: List[resenia.Resenia]

    # Método que devuelve todas las reseñas de un local dado
    def buscar_resenias_por_local(self, local):
        pass
