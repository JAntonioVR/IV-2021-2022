# Fichero de la clase Resenia, clase que modeliza una Reseña

from dataclasses import dataclass, field
from typing import List

@dataclass(frozen=True)
class Resenia:

    texto: str
    local_id: str     # cadena única para referenciar a un local
    puntuacion: int
    palabras_clave: List[str] = field(default_factory=list)

