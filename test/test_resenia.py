# encoding: utf-8
import os
import pytest
# import sys
# sys.path.append('./review_set')
from review_set.resenia import Resenia
from review_set.conjunto_resenias import ConjuntoResenias
from configuration.configuracion import read_config_file

def test_validacion_configparser():
    read_config_file('configuration/config.ini')
    
config = read_config_file('configuration/config.ini')

@pytest.fixture
def dataset():
    return config['dataset']

@pytest.fixture
def conjunto_resenias(dataset):
    return ConjuntoResenias(dataset)

def test_constructor_conjunto_resenias(dataset):
    '''
    Comprueba que el constructor de la clase ConjuntoResenia no devuelve un objeto nulo
    sino un objeto de la clase ConjuntoResenias y que no hay errores en la carga del
    conjunto de datos.
    '''
    test_dataset_name(dataset)
    review_set = ConjuntoResenias(dataset)
    assert(review_set != None and isinstance(review_set, ConjuntoResenias) and review_set.numero_resenias() >= 0)


def test_constructor_conjunto_resenias_nulo():
    '''
    Comprueba que el constructor de la clase ConjuntoResenia crea un conjunto vacío si
    no se especifica ningún dataset
    '''
    review_set = ConjuntoResenias()
    assert(review_set != None and isinstance(review_set, ConjuntoResenias) and review_set.numero_resenias() == 0)

def test_dataset_name(dataset):
    '''
    Comprueba que el fichero de datos existe.
    '''
    assert(os.path.isfile(dataset))

def test_buscar_resenias_por_local(conjunto_resenias):
    '''
    Comprueba que no hay errores en la búsqueda por local de la clase ConjuntoResenias.
    '''
    local_id = "The Food Kingdom"
    resenias_local = conjunto_resenias.buscar_resenias_por_local(local_id)
    res = True
    assert(isinstance(resenias_local, ConjuntoResenias))
    for resenia in resenias_local.resenias:
        res = res and (resenia.local_id == local_id)
    assert(res)

def test_instancias_conjunto(conjunto_resenias):
    '''
    Comprueba que todos los objetos que almacena 'conjunto_resenias' son de la clase
    Resenia.
    '''
    res = True
    for resenia in conjunto_resenias.resenias:
        res = res and isinstance(resenia, Resenia)
    assert(res)
    
def comprueba_texto_resenia(r):
    '''
    Comprueba que el atributo 'texto' de la reseña 'r' es una cadena de caracteres
    no vacía.
    '''
    texto = r.texto
    assert(isinstance(texto, str) and len(texto) > 0)

def comprueba_puntuacion_resenia(r):
    '''
    Comprueba que el atributo 'puntuacion' de la reseña 'r' es un entero entre 1 y 5.
    '''
    puntuacion = r.puntuacion
    assert(isinstance(puntuacion, int) and puntuacion > 0 and puntuacion <= 5 )

def comprueba_local_id_resenia(r):
    '''
    Comprueba que el atributo 'local_id' de la reseña 'r' es una cadena de caracteres
    no vacía.
    '''
    local_id = r.local_id
    assert(isinstance(local_id, str) and len(local_id) > 0)

def comprueba_resenia(r):
    '''
    Comprueba la integridad de los atributos de 'r'
    '''
    comprueba_texto_resenia(r)
    comprueba_puntuacion_resenia(r)
    comprueba_local_id_resenia(r)

def test_conjunto_resenias(conjunto_resenias):
    '''
    Comprueba la integridad de cada una de las reseñas de conjunto_resenias
    '''
    for i in range(conjunto_resenias.numero_resenias()):
        review = conjunto_resenias.buscar_resenia_por_indice(i)
        comprueba_resenia(review)

