# Fichero de la clase Aspectos, que encuentra y modela los aspectos positivos y negativos de un local en base a sus reseñas

from dataclasses import dataclass, field
from typing import List

import resenia

@dataclass
class Aspectos:

    resenias: List[resenia.Resenia]
    local: str
    aspectos_positivos: List[str] = field(default_factory=lambda: [])
    aspectos_negativos: List[str] = field(default_factory=lambda: [])

    # Método para extraer los aspectos positivos
    def extraer_aspectos_positivos(self):
        pass

    # Método para extraer los aspectos negativos
    def extraer_aspectos_negativos(self):
        pass
