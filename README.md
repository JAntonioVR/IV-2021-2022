# Proyecto IV
> Juan Antonio Villegas Recio 

## Descripción del problema
Todo dueño de un restaurante busca siempre no sólo su beneficio, sino también el bienestar de sus clientes, pudiendo recoger opiniones y reseñas y analizarlas para saber en qué mejorar. El objetivo de este proyecto es ofrecer un medio que a partir de la información proporcionada por parte de los clientes sugiera estrategias y decisiones que ayuden a mejorar el negocio y la experiencia de los consumidores. 

## Modelado
Utilizando las reseñas que los clientes interesados dejen con puntuación genérica (de 0 a 5 estrellas) y con un comentario se pueden sacar conclusiones de sus comentarios examinando y buscando palabras clave utilizando heurísticas de procesamiento de lenguaje natural. Con la información extraída de las reseñas se puede realizar un procesamiento que nos diga los aspectos negativos y positivos del restaurante que utilice esta plataforma, pudiendo así ofrecer estrategias de mejora.

## Documentación
En [este documento](./docs/personas.md) se describen los distintos usuarios potenciales, sus historias de usuario y los PMV.

En [este documento](./docs/lenguaje.md) se encuentra el lenguaje elegido y la justificación de dicha elección.

## Gestión de dependencias y de tareas
Se ha elegido utilizar el gestor de dependencias [`poetry`](https://python-poetry.org/), ya que es cómodo para trabajar en `Python` y ofrece la funcionalidad necesaria para instalar y tratar las dependencias de paquetes. Además, la [documentación de `poetry`](https://python-poetry.org/docs/) es completa y me ha resultado sencillo iniciarme en su uso. Sin embargo, `poetry` no es un *task runner* como tal, aunque puede simularse el comportamiento deseado de cierta manera. En lugar de ello he preferido utilizar el gestor de tareas [`invoke`](https://www.pyinvoke.org/), que permite con sencillos comandos ejecutar tareas previamente programadas o llamadas en bash. Todas las dependencias de paquetes necesarias hasta ahora se encuentran en el fichero [`pyproject.toml`](./pyproject.toml)

### Uso de `invoke`
Si se ejecuta la orden `invoke --list` podemos comprobar qué tareas están ya programadas:

```
$ invoke --list
Available tasks:

  add-dependency   Añade una nueva dependencia al fichero 'pyproject.toml'
  check            Comprueba la sintaxis de los ficheros de código
  ejecuta-docker   Ejecuta el contenedor de Docker para pasar los test
  install          Instala todas las dependencias
  install-no-dev   Instala las dependencias que NO son de desarrollador
  test             Ejecuta los test usando `pytest`
```

Más en profundidad:

* `invoke [--dev] [--package=STRING]`: Se añade, mediante poetry, una dependencia al fichero `pyproject.toml`, especificada por la opción `--package`. Si se indica la opción `--dev` (o `-d`) se añadirá a las dependencias de desarrollador.
* `invoke check`: Utilizando `py3compile`, comprueba la sintaxis de los ficheros de código y de las entidades programadas hasta el momento.
* `invoke ejecuta-docker`: Ejecuta los test utilizando un contenedor de Docker. Más información a continuación.
* `invoke install`: Instala todas las dependencias, sean o no de desarrollador.
* `invoke install-no-dev`: Instala solo las dependencias que **no** sean de desarrollador.
* `invoke test`: Lanza a ejecutar los test.

Para una información más concisa sobre alguna tarea concreta ejecutar `inv[oke] --help <task>` 

### Test

En el fichero `test/test_resenia.py` podemos encontrar las funciones implementadas como test. El objetivo es testear las clases `Resenia` y `ConjuntoResenias` junto con sus métodos. Estas dos clases están íntimamente relacionadas por composición, por lo que para el testeo de `ConjuntoResenias` es necesario también el testeo de `Resenia`. En el futuro, estas clases almacenarán la lógica para extraer los aspectos positivos y negativos del restaurante. En particular, `Resenia` contendrá los datos de una reseña junto con sus palabras clave. En esta fase del proyecto aún no se ha implementado la lógica necesaria para extraer palabras clave, por lo que simplemente testeamos el resto de atributos. Por su parte, `ConjuntoResenias` almacena reseñas y realiza algunas tareas de consulta, algunas de ellas ya implementadas y testeadas.

Como framework de test se ha utilizado el módulo `pytest`, versión `6.2.5` o posterior. Se ha utilizado dicha herramienta porque se integra de manera sencilla con `python` construyendo simplemente un fichero de test que el propio `pytest` ejecuta. La forma de ejecutarlo es simplemente utilizando el gestor de tareas mediante la orden:
```bash
$ inv[oke] test
```

## Contenedor para pruebas

Una vez implementados los test y automatizada su ejecución mediante el gestor de tareas, se encapsulará todo lo necesario para la ejecución de estos test en un contenedor de [**`Docker`**](https://www.docker.com/). La construcción del docker se puede ver modelada en el fichero [`Dockerfile`](./Dockerfile), aunque la explicaremos brevemente:

En un primer momento, se decidió un único contenedor base, cuya justificación se puede encontrar en [este fichero](./docs/contenedor_docker.md). Sin embargo, en siguientes versiones se permitió parametrizar la construcción del contenedor pudiendo probar distintas versiones de `python`, dejando como parámetro por defecto la versión primera: `python:3.8-slim`:

```Dockerfile
ARG PYTHON_VERSION=3.8-slim
FROM python:${PYTHON_VERSION}
```

* Como buena práctica, se ha creado un nuevo usuario `iv_app` y ejecutado los comandos con este, evitando así el uso del superusuario y los peligros que conlleva.

* Inicialmente se estableció como `WORKDIR` la carpeta `/home/iv-app` para la instalación de paquetes, pero realmente interesa que lo sea `app/test`, que es sobre la que se montarán los archivos y se ejecutará el código de los test.

Para la ejecución del contenedor bastaría con la ejecución de la orden:

```bash
docker run -t -v `pwd`:/app/test jantoniovr/iv-2021-2022:<version de Python>
```

O también se puede utilizar el gestor de tareas para ejecutar el contenedor mediante la orden:

```bash
inv[oke] ejecuta-docker -v <version de Python>
```

Este contenedor está continuamente sincronizado con DockerHub, mediante su propio repositorio [`jantoniovr/iv-2021-2022`](https://hub.docker.com/repository/docker/jantoniovr/iv-2021-2022), que coincide con el nombre de este. En DockerHub podemos encontrar imágenes para distintas versiones de python: `3.8`, `3.8-slim`, `3.9`, `3.9-slim`, `3.10`, `3.10-slim`. Se han usado estas versiones porque la 3.8 es la última versión estable de python y 3.10 es la última versión, y queremos comprobar el funcionamiento de nuestro proyecto en las versiones estándar y en las versiones slim, más ligeras.
