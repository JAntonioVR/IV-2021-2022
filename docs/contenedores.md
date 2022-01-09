# Contenedores para pruebas

Una vez implementados los test y automatizada su ejecución mediante el gestor de tareas, se encapsulará todo lo necesario para la ejecución de estos test en un contenedor de [**`Docker`**](https://www.docker.com/). La construcción del docker se puede ver modelada en el fichero [`Dockerfile`](../Dockerfile), aunque la explicaremos brevemente:

En un primer momento, se decidió un único contenedor base, cuya justificación se puede encontrar en [este fichero](./contenedor_docker.md). Sin embargo, en siguientes versiones se permitió parametrizar la construcción del contenedor pudiendo probar distintas versiones de `python` con distintos contenedores base, dejando como parámetro por defecto el contenedor base primero: `python:3.8-slim`:

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

Este contenedor y las distintas imágenes están continuamente sincronizados con DockerHub, mediante su propio repositorio [`jantoniovr/iv-2021-2022`](https://hub.docker.com/repository/docker/jantoniovr/iv-2021-2022), que coincide con el nombre de este. En DockerHub podemos encontrar imágenes utilizando distintos contenedores base con distintas versiones de python: `3.8-slim`, `3.9-slim` y `3.10-slim`. Se han usado estas versiones porque la 3.8 es la versión sobre la que se ha programado el código, es una versión estable y la más utilizada a día de hoy.  Por otra parte, la última versión es la 3.10, y queremos testear el código en todas las versiones intermedias, por tanto lo lógico es usar las versiones 3.8, 3.9 y 3.10. Por su parte,  Las versiones slim se caracterizan por contener lo mínimo necesario para ejecutar python, que es lo único que necesario antes de instalar las dependencias. Por ello, es deseable testear el código en los contenedores slim, que además son más ligeros y proporcionaron un mejor rendimiento en las pruebas ejecutadas (véase [esta documentación](./contenedor_docker.md)).