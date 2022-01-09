# Configuración y 'logging'

Se ha añadido funcionalidad para gestionar distintas configuraciones de la aplicación y registro de eventos (logging). Para ello, se han creado clases que abstraen todo el procesado, siguiendo los principios SOLID:

* Sobre **Configuración**: Podemos encontrar en el fichero `configuracion.py` la clase `Configuracion`, que lee del fichero `.env` todas las variables y las convierte en variables de entorno, las cuales lee e introduce en atributos a los que se puede acceder mediante los distintos 'getters'.
* Sobre **logging**: Podemos encontrar en el fichero `mylogger.py` la clase `MyLogger`, la cual lee los posibles parámetros del logging (como son el nivel de logging o el fichero de salida de los logs) a partir de la configuración y encapsula un logger que se usa como interfaz del logging.

También existe una clase `ConjuntoReseniaFactory`, que no es más que un wrapper de la clase `ConjuntoResenia`, que tiene sus mismos métodos, con los mismos argumentos y los mismos retornos, pero utilizando el logger anteriormente comentado para registrar los eventos que ocurren en la clase. Así, tenemos un nivel más alto de abstracción y garantizamos el cumplimiento del principio Open/Close.

## ¿Qué bibliotecas se han utilizado?

Necesitamos una biblioteca para configuración que acceda a ficheros .env de manera rápida e introducir las variables en atributos de manera sencilla. Hay varias alternativas:

1. Usar estructuras de datos propias: Es la opción más sencilla, mantener por ejemplo en un diccionario todas las variables de configuración y acceder a ellas desde el propio código. Sin embargo, esta técnica es muy sensible, pues no permite tener datos secretos en la configuración, pues estarían expuestos.
2. Usar un fichero de configuración: Almacena la configuración en ficheros YAML, JSON o INI, accediendo a dichos ficheros, que podrían estar ocultos o cifrados. Ésta es de hecho la manera más extendida de gestionar configuraciones. Algunas bibliotecas:
   * `config`: Es un módulo que permite, entre otras cosas, configuración jerárquica y referencias cruzadas dentro de la propia configuración. Además permite trabajar con variables de entorno y línea de comandos.
   * `configparser`: Utiliza fundamentalmente ficheros en formato INI, y a partir de estos se introducen las distintas opciones en una especie de objeto muy similar a un diccionario. Un punto a su favor es que viene integrada con el lenguaje, no es necesario incluirla en el gestor de dependencias.
3. Usar variables de entorno: No utiliza como tal ficheros, sino variables de entorno para configuración. Una opción es:
   * `dotenv`: Carga en variables de entorno del sistema los pares clave-valor de un posible fichero `.env`.

Inicialmente de hecho se tomó la decisión de utilizar `configparser` por su simplicidad, pero realmente la utilidad de las variables de entorno nos puede ayudar mucho en integración continua. Ocultamos el fichero `.env` utilizando `.gitignore` y así mantenemos nuestros secretos a salvo, pudiendo acceder a la configuración no sensible mediante variables de entorno. Por ello, finalmente se optó por utilizar variables de entorno y `dotenv` para la configuración. De esta forma, aunque los sistemas de integración continua no encuentren un fichero `.env`, se les puede especificar la configuración no sensible mediante variables de entorno, teniendo así el mismo comportamiento.

Para el logging necesitamos una herramienta que permita distintas parametrizaciones: el formato, el fichero de salida, el nivel, etc. A partir de esa parametrización, que de hecho obtendremos de la configuración, debe registrar los eventos que se le indiquen en el output deseado.

* Si queremos que el output tenga formato JSON podemos usar [`python-json-logger`](https://github.com/madzak/python-json-logger), una librería que permite escribir ficheros de logging en formato json, permitiendo a su vez personalizar los campos.
* [`logging`](https://docs.python.org/3/library/logging.html) es el logger estándar de Python, que es sencillo, personalizable y viene incluido en el propio lenguaje. Es la opción más usada por la comunidad.
* El módulo [`django`](https://www.djangoproject.com/), que es un conocido framework de desarrollo web, incluye amplias posibilidades de logging, incluyendo logs para peticiones, para servidores o para base de datos. Está basado en el módulo `logging` estándar y es muy útil en despliegue.
* [`Flask`](https://flask.palletsprojects.com/en/2.0.x/) es el segundo framework web más conocido para Python, más sencillo que `django`. `Flask` utiliza también el `logging` estándar de Python, pero al contrario que `django` sólo utiliza un logger llamado [`app.logger`](https://flask.palletsprojects.com/en/1.1.x/api/#flask.Flask.logger).
* El módulo  [`Twisted`](https://twistedmatrix.com/trac/) es un framework de red asíncrono y basado en eventos ('event-driven'). Su framework de logging es similar a otros pero tiene una diferencia principal: Los eventos que se registran en `Twisted` se generan a partir de diccionarios, no de strings, lo cual favorece el uso de formatos como JSON.
* [`VizTracer`](https://github.com/gaogaotiantian/viztracer?ref=pythonrepo.com) es una herramienta útil no solo para 'logging' sino también para 'debugging' y para 'profiling' en la que se puede visualizar la ejecución de código Python. Fácilmente instalable (un sólo módulo), sin dependencias de otros paquetes y sencilla de usar. Parece buena opción, pero aún está en fase de desarrollo y es poco conocida, por lo que es probable que tenga fallos y código susceptible a cambios.

Además de estas opciones, realmente muchos de los grandes frameworks de Python para cualquier ámbito, como desarrollo web, cálculo numérico o ciencia de datos incorporan su propio sistema de 'logging'.

En fases avanzadas del proyecto, probablemente la mejor opción sea la de `django` o `flask`, para poder registrar todo tipo de eventos relacionados con la infraestructura virtual. Sin embargo, en esta fase del proyecto es suficiente con utilizar la librería `logging` estándar, pues cumple con todos los requisitos expuestos y no requiere ninguna dependencia adicional.
