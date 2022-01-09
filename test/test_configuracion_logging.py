
import pytest
from review_set.conjunto_resenias import ConjuntoReseniasFactory
from configuracion import Configuracion
from mylogger import levels
from re import match, MULTILINE


@pytest.fixture
def configuracion():
    return Configuracion()

def test_logging_file(configuracion):
    '''
    Comprueba que en caso de especificarse un archivo de logging su ruta no es una cadena
    vacía.
    '''
    logging_file = configuracion.get_logging_path()
    if(logging_file):
        assert(len(logging_file) > 0)

def test_logging_level(configuracion):
    '''
    Comprueba que el nivel de configuración es una de las constantes predefinidas.
    '''
    assert(configuracion.get_logging_level() in levels)

def test_logging(configuracion):
    cr = ConjuntoReseniasFactory(configuracion.get_dataset())
    cr.buscar_resenias_por_local('Sweet and Tasty')
    cr.buscar_resenias_por_local('AAAAAA')
    cr.buscar_resenia_por_indice(0)
    cr.buscar_resenia_por_indice(400)
    file = open(configuracion.get_logging_path(),'r')
    assert( match(r"^((DEBUG|INFO|WARNING|ERROR|CRITICAL) - [\d\D]*){8}", file.read(), MULTILINE) != None )
