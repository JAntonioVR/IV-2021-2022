# Integración continua

A partir de las distintas imágenes creadas y subidas a DockerHub, conviene integrar la ejecución de los test en las distintas versiones de Python con cada subida a github. Para ello, se han configurado varios **sistemas de integración continua**. Concretamente:

* Se ha hecho uso de [**Circle CI**](https://circleci.com/) como sistema de CI que ejecuta en paralelo los tests para las versiones 3.9 y 3.10 de Python, utilizando los contenedores base `Python:3.9-slim` y `Python:3.10-slim`.
* Se ha hecho uso de [**Github Actions**](https://github.com/features/actions) como sistema de CI que ejecuta los tests empleando la versión por defecto: la versión 3.8 utilizando el contenedor base `Python:3.8-slim`.

## Por qué Circle CI y Github Actions

Existen muchas y variadas herramientas de integración continua y cada una tiene sus ventajas e inconvenientes. En [este enlace](https://bitbar.com/blog/top-continuous-integration-tools-for-devops/) se puede encontrar un listado de sistemas de integración continua e información de cada una. Para un desarrollador con poca (o en mi caso ninguna) experiencia en el uso de integración continua es importante utilizar una herramienta con buena documentación, con tutoriales ejemplificadores y con sintaxis sencilla, empleando estos como principales criterios de búsqueda. Se estudió la posibilidad de utilizar, además de las utilizadas finalmente, las siguientes:

* [**Jenkins**](https://jenkins.io/): Es muy popular y muy utilizada en desarrollo de software, además de incluir una buena documentación, aunque requiere instalación y parece una herramienta demasiado compleja para el objetivo actual de nuestra CI.
* [**Semaphore CI**](https://semaphoreci.com/): Es una herramienta similar a Circle, CI en el sentido de que no es necesario descargar ni instalar nada en el PC, se puede gestionar la CI al completo desde el navegador. Se consideró seria candidata esta herramienta, pero es privativa e inicialmente incluye únicamente 14 días gratuitos.
* [**Travis CI**](https://travis-ci.org/): Es la herramienta por excelencia para iniciarse en el mundo de la integración continua, gracias a una sencilla sintaxis y uso. Sin embargo, los minutos gratuitos están limitados y es necesario ingresar tarjeta de crédito para poder empezar a usarlo.
* [**GitLab CI**](https://docs.gitlab.com/ee/ci/): Aparentemente es una herramienta popular y muy utilizada con muy buena documentación, pero tampoco es gratuita y requiere instalación.

Sin embargo, tanto Github Actions como Circle CI son herramientas con una muy buena documentación, que no requieren instalación y sencillas de integrar con GitHub. En concreto, GitHub Actions está naturalmente integrada con GitHub y Circle CI desde el primer momento fue sencillo configurarlo para que empezara a funcionar sobre el repositorio. Respecto a la sintaxis, la de Circle CI es más sencilla que la de Actions, además de ser fácil de utilizar gracias a su documentación y a los tutoriales. Por su parte, GitHub Actions tiene una sintaxis más compleja, pero aprendida gracias al uso de esta herramienta en la subida del contenedor a dockerhub, además de contar con muchas actions predefinidas que solucionan en gran medida los problemas. 

En definitiva, aunque las opciones son muchas y muy variadas, de acuerdo a mis criterios las más adecuadas al proyecto son **Circle CI** y **GitHub Actions**.
