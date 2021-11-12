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
  install          Instala todas las dependencias
  install-no-dev   Instala las dependencias que NO son de desarrollador
  test             Lanza a ejecutar los test
```

Más en profundidad:

* `invoke [--dev] [--package=STRING]`: Se añade, mediante poetry, una dependencia al fichero `pyproject.toml`, especificada por la opción `--package`. Si se indica la opción `--dev` (o `-d`) se añadirá a las dependencias de desarrollador.
* `invoke check`: Utilizando `py3compile`, comprueba la sintaxis de los ficheros de código y de las entidades programadas hasta el momento.
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
