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

En un primer momento, se decidió un único contenedor base, cuya justificación se puede encontrar en [este fichero](./docs/contenedor_docker.md). Sin embargo, en siguientes versiones se permitió parametrizar la construcción del contenedor pudiendo probar distintas versiones de `python` con distintos contenedores base, dejando como parámetro por defecto el contenedor base primero: `python:3.8-slim`:

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

Este contenedor y las distintas imágenes están continuamente sincronizados con DockerHub, mediante su propio repositorio [`jantoniovr/iv-2021-2022`](https://hub.docker.com/repository/docker/jantoniovr/iv-2021-2022), que coincide con el nombre de este. En DockerHub podemos encontrar imágenes utilizando distintos contenedores base con distintas versiones de python: `3.8-slim`, `3.9-slim` y `3.10-slim`. Se han usado estas versiones porque la 3.8 es la versión sobre la que se ha programado el código, es una versión estable y la más utilizada a día de hoy.  Por otra parte, la última versión es la 3.10, y queremos testear el código en todas las versiones intermedias, por tanto lo lógico es usar las versiones 3.8, 3.9 y 3.10. Por su parte,  Las versiones slim se caracterizan por contener lo mínimo necesario para ejecutar python, que es lo único que necesario antes de instalar las dependencias. Por ello, es deseable testear el código en los contenedores slim, que además son más ligeros y proporcionaron un mejor rendimiento en las pruebas ejecutadas (véase [esta documentación](docs/contenedor_docker.md)).

## Integración continua

A partir de las distintas imágenes creadas y subidas a DockerHub, conviene integrar la ejecución de los test en las distintas versiones de Python con cada subida a github. Para ello, se han configurado varios **sistemas de integración continua**. Concretamente:

* Se ha hecho uso de [**Circle CI**](https://circleci.com/) como sistema de CI que ejecuta en paralelo los tests para las versiones 3.9 y 3.10 de Python, utilizando los contenedores base `Python:3.9-slim` y `Python:3.10-slim`.
* Se ha hecho uso de [**Github Actions**](https://github.com/features/actions) como sistema de CI que ejecuta los tests empleando la versión por defecto: la versión 3.8 utilizando el contenedor base `Python:3.8-slim`.

### Por qué Circle CI y Github Actions

Existen muchas y variadas herramientas de integración continua y cada una tiene sus ventajas e inconvenientes. En [este enlace](https://bitbar.com/blog/top-continuous-integration-tools-for-devops/) se puede encontrar un listado de sistemas de integración continua e información de cada una. Para un desarrollador con poca (o en mi caso ninguna) experiencia en el uso de integración continua es importante utilizar una herramienta con buena documentación, con tutoriales ejemplificadores y con sintaxis sencilla, empleando estos como principales criterios de búsqueda. Se estudió la posibilidad de utilizar, además de las utilizadas finalmente, las siguientes:

* [**Jenkins**](https://jenkins.io/): Es muy popular y muy utilizada en desarrollo de software, además de incluir una buena documentación, aunque requiere instalación y parece una herramienta demasiado compleja para el objetivo actual de nuestra CI.
* [**Semaphore CI**](https://semaphoreci.com/): Es una herramienta similar a Circle, CI en el sentido de que no es necesario descargar ni instalar nada en el PC, se puede gestionar la CI al completo desde el navegador. Se consideró seria candidata esta herramienta, pero es privativa e inicialmente incluye únicamente 14 días gratuitos.
* [**Travis CI**](https://travis-ci.org/): Es la herramienta por excelencia para iniciarse en el mundo de la integración continua, gracias a una sencilla sintaxis y uso. Sin embargo, los minutos gratuitos están limitados y es necesario ingresar tarjeta de crédito para poder empezar a usarlo.
* [**GitLab CI**](https://docs.gitlab.com/ee/ci/): Aparentemente es una herramienta popular y muy utilizada con muy buena documentación, pero tampoco es gratuita y requiere instalación.

Sin embargo, tanto Github Actions como Circle CI son herramientas con una muy buena documentación, que no requieren instalación y sencillas de integrar con GitHub. En concreto, GitHub Actions está naturalmente integrada con GitHub y Circle CI desde el primer momento fue sencillo configurarlo para que empezara a funcionar sobre el repositorio. Respecto a la sintaxis, la de Circle CI es más sencilla que la de Actions, además de ser fácil de utilizar gracias a su documentación y a los tutoriales. Por su parte, GitHub Actions tiene una sintaxis más compleja, pero aprendida gracias al uso de esta herramienta en la subida del contenedor a dockerhub, además de contar con muchas actions predefinidas que solucionan en gran medida los problemas. 

En definitiva, aunque las opciones son muchas y muy variadas, de acuerdo a mis criterios las más adecuadas al proyecto son **Circle CI** y **GitHub Actions**.

## Configuración y 'logging'

Se ha añadido funcionalidad para gestionar distintas configuraciones de la aplicación y registro de eventos (logging). Para ello, se han creado clases que abstraen todo el procesado, siguiendo los principios SOLID:

* Sobre **Configuración**: Podemos encontrar en el fichero `configuracion.py` la clase `Configuracion`, que lee del fichero `.env` todas las variables y las convierte en variables de entorno, las cuales lee e introduce en atributos a los que se puede acceder mediante los distintos 'getters'.
* Sobre **logging**: Podemos encontrar en el fichero `mylogging.py` la clase `MyLogger`, la cual lee los posibles parámetros del logging (como son el nivel de logging o el fichero de salida de los logs) a partir de la configuración y encapsula un logger que se usa como interfaz del logging.

También existe una clase `ConjuntoReseniaFactory`, que no es más que un wrapper de la clase `ConjuntoResenia`, que tiene sus mismos métodos, con los mismos argumentos y los mismos retornos, pero utilizando el logger anteriormente comentado para registrar los eventos que ocurren en la clase. Así, tenemos un nivel más alto de abstracción y garantizamos el cumplimiento del principio Open/Close.

### ¿Qué bibliotecas se han utilizado?

Necesitamos una biblioteca para configuración que acceda a ficheros .env de manera rápida e introducir las variables en atributos de manera sencilla. Hay varias alternativas:

1. Usar estructuras de datos propias: Es la opción más sencilla, mantener por ejemplo en un diccionario todas las variables de configuración y acceder a ellas desde el propio código. Sin embargo, esta técnica es muy sensible, pues no permite tener datos secretos en la configuración, pues estarían expuestos.
2. Usar un fichero de configuración: Almacena la configuración en ficheros YAML, JSON o INI, accediendo a dichos ficheros, que podrían estar ocultos o cifrados. Ésta es de hecho la manera más extendida de gestionar configuraciones. Algunas bibliotecas:
   * `config`: Es un módulo que permite, entre otras cosas, configuración jerárquica y referencias cruzadas dentro de la propia configuración. Además permite trabajar con variables de entorno y línea de comandos.
   * `configparser`: Utiliza fundamentalmente ficheros en formato INI, y a partir de estos se introducen las distintas opciones en una especie de objeto muy similar a un diccionario. Un punto a su favor es que viene integrada con el lenguaje, no es necesario incluirla en el gestor de dependencias.
3. Usar variables de entorno: No utiliza como tal ficheros, sino variables de entorno para configuración. Una opción es:
  * `dotenv`: Carga en variables de entorno del sistema los pares clave-valor de un posible fichero `.env`.

Inicialmente de hecho se tomó la decisión de utilizar `configparser` por su simplicidad, pero realmente la utilidad de las variables de entorno nos puede ayudar mucho en integración continua. Ocultamos el fichero `.env` utilizando `.gitignore` y así mantenemos nuestros secretos a salvo, pudiendo acceder a la configuración no sensible mediante variables de entorno. Por ello, finalmente se optó por utilizar variables de entorno y `dotenv` para la configuración.

Para el logging necesitamos una herramienta que permita distintas parametrizaciones: el formato, el fichero de salida, el nivel, etc. A partir de esa parametrización, que de hecho obtendremos de la configuración, debe registrar los eventos que se le indiquen en el output deseado.

* Si queremos que el output tenga formato JSON podemos usar `python-json-logger`, una librería que permite escribir ficheros de logging en formato json, permitiendo a su vez personalizar los campos.
* `logging` es el logger estándar de Python, que es sencillo, personalizable y viene incluido en el propio lenguaje. Es la opción más usada por la comunidad.
* El módulo `django`, que es un conocido framework de desarrollo web, incluye amplias posibilidades de logging, incluyendo logs para peticiones, para servidores o para base de datos. Está basado en el módulo `logging` estándar y es muy útil en despliegue.

En fases avanzadas del proyecto, probablemente la mejor opción sea la última, para poder registrar todo tipo de eventos relacionados con la infraestructura virtual. Sin embargo, en esta fase del proyecto es suficiente con utilizar la librería `logging` estándar, pues cumple con todos los requisitos expuestos y no requiere ninguna dependencia adicional.
