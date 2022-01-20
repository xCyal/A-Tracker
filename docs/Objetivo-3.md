# Elección de task runner:
## Invoke

Invoke es un task runner en python que nos permite definir y ejecutar tareas sobre nuestro proyecto. Se puede invocar las funciones de las tareas de manera muy similar a make (inv <funcion>) por lo que es bastante cómodo para usuarios acostumbrados a este último. Además su documentación es bastante completa y sencilla, por lo que se vuelve fácil trabajar con invoke. 

La elección de invoke como task runner se ha tomado en base a lo mencionado previamente, especialmente por su parecido con make a la vez que nos permite definir las funciones al estilo de python.

  
# Gestión de dependencias
  
El proyecto utiliza [poetry](https://python-poetry.org/docs/) para gestionar las dependencias del mismo. Se trata de un software escrito en python que permite la gestión de dependencias y paquetes del lenguaje de manera cómoda y eficaz, encargandose de su instalanción y actualización. Para poder manejar dichas dependencias, se hace uso del archivo pyproject.toml donde se especifican. También aporta la posibilidad de crear entornos de desarrollo con las distintas versiones del software que estemos utilizando y nos permite lanzar ordenes dentro de los mismos.
 
