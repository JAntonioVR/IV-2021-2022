import os

import sys
sys.path.append('./review_set')
from resenia import Resenia
from conjunto_resenias import ConjuntoResenias

def test_constructor_conjunto_resenias():
    '''
    Comprueba que el constructor de la clase ConjuntoResenia no devuelve un objeto nulo
    sino un objeto de la clase ConjuntoResenias.
    '''
    review_set = ConjuntoResenias(None)
    assert(review_set != None and isinstance(review_set, ConjuntoResenias))

def test_dataset_name(dataset: str):
    '''
    Comprueba que el fichero de nombre 'dataset' existe.
    '''
    assert(os.path.isfile(dataset))

def test_carga_datos(dataset: str):
    '''
    Comprueba que no hay errores en la carga de los datos de la clase ConjuntoResenias.
    '''
    test_dataset_name(dataset)
    review_set = ConjuntoResenias(None)
    review_set.carga_datos(dataset)
    assert(review_set.numero_resenias() >= 0)

def test_buscar_resenias_por_local(conjunto_resenias: ConjuntoResenias,local_id: str):
    '''
    Comprueba que no hay errores en la búsqueda por local de la clase ConjuntoResenias.
    '''
    resenias_tfk = conjunto_resenias.buscar_resenias_por_local(local_id)
    res = True
    assert(isinstance(resenias_tfk, ConjuntoResenias))
    for i in range(resenias_tfk.numero_resenias()):
        review = resenias_tfk.buscar_resenia_por_indice(i)
        res = res and (review.local_id == local_id)
    assert(res)

def test_instancias_conjunto(conjunto_resenias: ConjuntoResenias):
    '''
    Comprueba que todos los objetos que almacena 'conjunto_resenias' son de la clase
    Resenia.
    '''
    res = True
    for i in range(conjunto_resenias.numero_resenias()):
        review = conjunto_resenias.buscar_resenia_por_indice(i)
        res = res and isinstance(review, Resenia)
    assert(res)
    
def test_texto_resenia(r: Resenia):
    '''
    Comprueba que el atributo 'texto' de la reseña 'r' es una cadena de caracteres
    no vacía.
    '''
    texto = r.texto
    assert(isinstance(texto, str) and len(texto) > 0)

def test_puntuacion_resenia(r: Resenia):
    '''
    Comprueba que el atributo 'puntuacion' de la reseña 'r' es un entero entre 1 y 5.
    '''
    puntuacion = r.puntuacion
    assert(isinstance(puntuacion, int) and puntuacion > 0 and puntuacion <= 5 )

def test_local_id_resenia(r: Resenia):
    '''
    Comprueba que el atributo 'local_id' de la reseña 'r' es una cadena de caracteres
    no vacía.
    '''
    local_id = r.local_id
    assert(isinstance(local_id, str) and len(local_id) > 0)

def test_resenia(r: Resenia):
    '''
    Comprueba la integridad de los atributos de 'r'
    '''
    test_texto_resenia(r)
    test_puntuacion_resenia(r)
    test_local_id_resenia(r)

def test_conjunto_resenias(conjunto_resenias: ConjuntoResenias):
    '''
    Comprueba la integridad de cada una de las reseñas de conjunto_resenias
    '''
    for i in range(conjunto_resenias.numero_resenias()):
        review = conjunto_resenias.buscar_resenia_por_indice(i)
        test_resenia(review)
