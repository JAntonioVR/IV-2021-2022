# Requisitos

* Se necesita un contenedor con soporte para ejecutar código de python y una herramienta para ejecutar el gestor de dependencias. En nuestro caso esta herramienta es `pip`.
* Al ser un contenedor cuyo principal objetivo es ejecutar unos tests, la funcionalidad es limitada. Por tanto buscaremos tener un contenedor de tamaño reducido.
* Sincronizaremos cada push con una construcción y sincronización con el repositorio asociado de `dockerhub`, por lo que también conviene una construcción rápida.


# Parámetros de búsqueda

Nos centraremos por tanto en buscar un contenedor base que nos proporcione una imagen ligera y rápida de construir.

En `dockerhub` hay muchas posibilidades, pero tomaremos la decisión de centrarnos en las imágenes oficiales de Python, por ser considerado buena práctica al ser actualizadas regularmente y más seguras que las imágenes no oficiales.

Las opciones principales son: `python:<version>`, `python:<version>-slim`, `python:<version>-alpine`.

Al utilizar sistema operativo linux hasta el momento y al haber diseñado el contenedor para ejecutarse en linux, considero que utilizar como base el `windowsservercore` no es la mejor opción. Por otro lado, gestionar las dependencias en la versión `alpine` es más difícil, cuando realmente tenemos muy pocas dependencias y fáciles de gestionar. 

Por ello, dudamos entre `python:<version>` y `python:<version>:slim`. Haremos pruebas basadas en estos parámetros para elegir finalmente la versión a utilizar.

# Pruebas

A favor de la versión 3.9 de python: Es la última versión estable con todas las garantías que eso implica a nivel de mantenimiento, además de la corrección de algunos bugs de la versión 3.8 (fuente: [docs.python](https://docs.python.org/3/whatsnew/3.9.html)).

A favor de la versión 3.8 de pyhton: Es la versión instalada en el ordenador local y con la cual se han programado las clases y los tests. Sin embargo, el código hasta ahora no tiene ninguna dependencia fuerte de la versión 3.8 respecto a la 3.9.

Comprobaremos el tiempo de construcción (en local), el tiempo de ejecución de los test, el tiempo de subida a dockerhub y el tamaño de las imágenes comprimidas en dockerhub:

| **Contenedor base** | **Tiempo de construcción**                             | **Tiempo de subida**                                   | **Tiempo de ejecución de test** | **Tamaño de la imagen comprimida** |
|-----------------|----------------------------------------------------|----------------------------------------------------|-----------------------------|--------------------------------|
| `python:3.8`      	| real    0m0,876s<br>user    0m0,191s<br>sys     0m0,162s 	| real    0m4,424s<br>user    0m0,043s<br>sys     0m0,013s 	| 0.05 s                      	| 364.1 MB                       	|
| `python:3.8-slim` 	| real    0m0,680s<br>user    0m0,245s<br>sys     0m0,130s 	| real    0m3,527s<br>user    0m0,030s<br>sys     0m0,028s 	| 0.05 s                      	| 364.1 MB                       	|
| `python:3.9`      	| real    0m0,781s<br>user    0m0,237s<br>sys     0m0,134s 	| real    0m3,759s<br>user    0m0,026s<br>sys     0m0,032s 	| 0.05 s                      	| 364.1 MB                       	|
| `python:3.9-slim` 	| real    0m0,606s<br>user    0m0,215s<br>sys     0m0,151s 	| real    0m4,171s<br>user    0m0,016s<br>sys     0m0,038s 	| 0.04 s   

Como vemos, el tiempo de ejecución de los tests y el tamaño de la imagen no es significativo, por lo que nos centraremos en el tiempo de construcción y subida. Las versiones construidas utilizando versiones slim como base son claramente más rápidas al construir, y como vemos es más rápida la subida utilizando la versión 3.8, por lo que en base a nuestros criterios y a nuestras pruebas consideramos el uso del contenedor base **`python:3.8-slim`**.