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


# ─── TEST ───────────────────────────────────────────────────────────────────────
@task
def test(c):
    '''
    Ejecuta los test usando `pytest`
    '''
    c.run("pytest")


# ─── EJECUTA CONTENEDOR DOCKER ──────────────────────────────────────────────────
@task
def ejecuta_docker(c, version):
    '''
    Ejecuta el contenedor de Docker para pasar los test
    '''
    c.run("docker run -t -v `pwd`:/app/test jantoniovr/iv-2021-2022:" + str(version))

# ────────────────────────────────────────────────────────────────────────────────
