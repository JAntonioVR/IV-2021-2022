# Fichero de la clase Resenia, clase que modeliza una Reseña

from dataclasses import dataclass, field
from typing import List

@dataclass(frozen=True)
class Resenia:
    '''Clase que modela una reseña.
    
    Atributos:
    texto (string): Texto de la reseña.
    local_id (string): Cadena única que referencia e identifica a un local.
    puntuacion (int): Puntuación dada en la reseña.
    palabras_clave (List[string]): Palabras de la reseña.
    '''

    texto: str
    local_id: str
    puntuacion: int
    palabras_clave: List[str] = field(default_factory=list)
