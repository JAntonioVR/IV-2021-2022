from invoke import task

import sys
sys.path.append('./test')
import test_hello_world

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

@task
def test(c):
    '''
    Lanza a ejecutar los test
    '''
    print("Ejecutando test...")
    test_hello_world.hello_world()
    