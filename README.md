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
Se ha utilizado `Poetry` como gestor de dependencias y el módulo `invoke` como gestor de tareas. Más información en [este documento](./docs/poetry_e_invoke.md)

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

## Contenido adicional

* **Testeo**: Todo el código del proyecto ha sido testeado. Información sobre el testeo y las herramientas utilizadas en [este documento](./docs/test.md).
* **Contenedor para pruebas**: Se han utilizado contenedores de `Docker` para ejecutar los tests. Más información en [este documento](./docs/contenedores.md).
* **Integración continua**: Se ha integrado la ejecución de los tests mediante contenedores con el uso de sistemas de integración continua. Más información en [este documento](./docs/integracion_continua.md).
* **Configuración y 'logging'**: Se ha incluido funcionalidad para parametrizar la configuración y el registro de eventos. Más información en [este documento](./docs/configuracion_logging.md).
