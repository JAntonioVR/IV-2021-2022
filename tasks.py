#
# ──────────────────────────────────────────────────────────────
#   :::::: test.py : :  :   :    :     :        :          :
# ──────────────────────────────────────────────────────────────
#

# ─── PROJECT: IV-2021-2022 (https://github.com/JAntonioVR/IV-2021-2022) ─────────
# ─── OWNER: @JAntonioVR ─────────────────────────────────────────────────────────
# ─── AUTHOR: @JAntonioVR ────────────────────────────────────────────────────────
# ─── DATE: 20-10-2021 ───────────────────────────────────────────────────────────
# ─── VERSION: 1.0 ───────────────────────────────────────────────────────────────

# Importamos invoke
from invoke import task

# Importamos el fichero de test que se encuentra en la carpeta 'test'
import sys
sys.path.append('./test')
from test_resenia import test_constructor_conjunto_resenias, test_dataset_name, test_carga_datos, test_conjunto_resenias, test_buscar_resenias_por_local

sys.path.append('./review_set')
from conjunto_resenias import ConjuntoResenias

# ─── INSTALACIÓN DE TODAS LAS DEPENDENCIAS ──────────────────────────────────────
@task
def install(c):
    '''
    Instala todas las dependencias
    '''
    print("Instalando dependencias...")
    result = c.run("poetry install")
    if(result):
        print("Dependencias instaladas con éxito.")
    else:
        print("Ha ocurrido algún error en la instalación.")


# ─── INSTALACIÓN DE DEPENDENCIAS QUE NO SON DE DESARROLLADOR ────────────────────
@task
def install_no_dev(c):
    '''
    Instala las dependencias que NO son de desarrollador
    '''
    print("Instalando dependencias que no son de desarrollador...")
    result = c.run("poetry install --no-dev")
    if(result):
        print("Dependencias instaladas con éxito.")
    else:
        print("Ha ocurrido algún error en la instalación.")


# ─── AÑADIR DEPENDENCIA ─────────────────────────────────────────────────────────
@task(help={'package': "Paquete que se desea añadir como dependencia",
            'dev':     "True si se desea añadir la dependencia como de desarrollador, False en otro caso"})
def add_dependency(c, package, dev=False):
    '''
    Añade una nueva dependencia al fichero 'pyproject.toml'
    '''
    print("Añadiendo dependencia...")
    if(dev):
        result = c.run("poetry add --dev " + package)
    else:
        result = c.run("poetry add" + package)

    if(result):
        print("Dependencia añadida con éxito")
    else:
        print("Ha ocurrido algún error al añadir la dependencia")


# ─── EJECUTAR TESTS ─────────────────────────────────────────────────────────────
@task
def test(c):
    '''
    Lanza a ejecutar los test
    '''
    print("─── EJECUTANDO TEST ────────────────────────────────────────────────────────────")
    print("Ejecutando test de constructor de ConjuntoResenias...")
    test_constructor_conjunto_resenias()
    print("OK")

    dataset = "./data/Restaurant_Reviews.tsv"

    print("Ejecutando test de comprobación de existencia del dataset Restaurant_Reviews.tsv...")
    test_dataset_name(dataset)
    print("OK")

    print("Ejecutando test de carga de datos...")
    test_carga_datos(dataset)
    print("OK")

    conjunto_resenias = ConjuntoResenias(None)
    conjunto_resenias.carga_datos(dataset)

    print("Ejecutando test de integridad del conjunto de reseñas...")
    test_conjunto_resenias(conjunto_resenias)
    print("OK")

    print("Ejecutando test de búsqueda por local...")
    test_buscar_resenias_por_local(conjunto_resenias, "The Food Kingdom")
    print("OK")

    print("─── TODOS LOS TEST HAN SIDO SUPERADOS ──────────────────────────────────────────") 





# ─── COMPROBAR SINTAXIS ─────────────────────────────────────────────────────────
@task
def check(c):
    '''
    Comprueba la sintaxis de los ficheros de código
    '''
    module = "resenia"
    print("Comprobando sintaxis...")
    if(c.run("py3compile " + module)):
        print("OK")
    
            
        
    
# ────────────────────────────────────────────────────────────────────────────────
