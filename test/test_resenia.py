import os

import sys
sys.path.append('./review_set')
from resenia import Resenia
from conjunto_resenias import ConjuntoResenias

def test_constructor_conjunto_resenias():
    review_set = ConjuntoResenias(None)
    assert(review_set != None)

def test_dataset_name(dataset: str):
    assert(os.path.isfile(dataset))

def test_carga_datos(dataset: str):
    review_set = ConjuntoResenias(None)
    review_set.carga_datos(dataset)
    assert(review_set.numero_resenias() >= 0)

def test_buscar_resenias_por_local(conjunto_resenias: ConjuntoResenias,local_id: str):
    resenias_tfk = conjunto_resenias.buscar_resenias_por_local(local_id)
    res = True
    assert(isinstance(resenias_tfk, ConjuntoResenias))
    for i in range(resenias_tfk.numero_resenias()):
        review = resenias_tfk.buscar_resenia_por_indice(i)
        res = res and (review.local_id == local_id)
    assert(res)

def test_instancias_conjunto(conjunto_resenias: ConjuntoResenias):
    res = True
    for i in range(conjunto_resenias.numero_resenias()):
        review = conjunto_resenias.buscar_resenia_por_indice(i)
        res = res and isinstance(review, Resenia)
    assert(res)
    
def test_texto_resenia(r: Resenia):
    texto = r.texto
    assert(isinstance(texto, str) and len(texto) > 0)

def test_puntuacion_resenia(r: Resenia):
    puntuacion = r.puntuacion
    assert(isinstance(puntuacion, int) and puntuacion > 0 and puntuacion <= 5 )

def test_local_id_resenia(r: Resenia):
    local_id = r.local_id
    assert(isinstance(local_id, str) and len(local_id) > 0)

def test_resenia(r: Resenia):
    test_texto_resenia(r)
    test_puntuacion_resenia(r)
    test_local_id_resenia(r)

def test_conjunto_resenias(conjunto_resenias: ConjuntoResenias):
    for i in range(conjunto_resenias.numero_resenias()):
        review = conjunto_resenias.buscar_resenia_por_indice(i)
        test_resenia(review)
