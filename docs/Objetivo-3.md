# Task Runner

## Criterios de elección

Vamos a establecer los criterios de elección del task runner de este proyecto sobre los que valoraremos las diferentes opciones disponibles:

- Menor número de dependencias adicionales.

- Lenguaje del Task Runner, preferiblemente python por simplicidad.

- Dificultad de ponerlo en marcha, si necesita configuración adicional.

- Forma de manejar el Task Runner, si es en un solo archivo o es algo más complejo.

- Documentación. ¿Se trata de una buena documentación, capaz de resolver dudas de manera clara? ¿Es extensa y explica correctamente como utilizar la herramienta?

- Recomendación de la comunidad, aunque no es fácil de evaluar, pero en caso de duda puede ser determinante.


### Task Runners que he revisado para realizar la elección: 

- [Make](https://www.gnu.org/software/make/manual/make.html) (Puede servir como Task runner, aunque su principal uso no es como tal, puede ser una buena opción):
  - Manejo desde un solo archivo Makefile.
  - No hay ninguna dificultad en su configuración.
  - No es específico de python. ❎
  - Sintaxis sencilla.

- [Doit](https://pydoit.org/contents.html):
  - Específico para python
  - Incluye dependencias externas ❎
  - Configuración en un fichero propio. 

- [Poethepoet](https://github.com/nat-n/poethepoet):
  - Específico para python
  - Incluye dependencias externas ❎
  - Configuración algo más complicada que el resto ❎
  - Configuración en pyproject.toml ❎📎 (Preferible un fichero propio, de forma que se encuentre separado el gestor de dependencias de el Task Runner)

He de mencionar que he encontrado otros como [Pypyr](https://pypyr.io/docs/) o [Taskipy](https://github.com/illBeRoy/taskipy), los cuales no parecen tener carácteristicas novedosas respecto a los anteriores además de encontrar bastante menos documentación sobre ellos.

Los aquí mencionados, se han descartado principalmente por los puntos marcados (❎), o bien tienen dependencias externas, no son específicos para python, o su configuración puede no ser tan sencilla como en Invoke e incluso en casos como Taskipy o Poethepoet depender directamente de pyproject.toml. Además las comunidades que respaldan a estos Task runners son considerablemente menores y su uso mucho menos extendido que el de Invoke.

## Invoke

Invoke es un "task execution tool & library", es decir, un software escrito en python que nos permite automatizar tareas sobre nuestros proyectos. Para ello utiliza un archivo llamado tasks.py sobre el cual se escriben las funciones deseadas (en el caso de este proyecto la función check, encargada de comprobar que el código de tracker compila), para más tarde poder invocar dichas funciones mediante el comando : - inv -funcion-

La razón del uso de invoke en nuestro proyecto viene dada por los siguientes motivos:

- No tiene dependencias adicionales.

- Específico para el lenguaje del proyecto (Python).

- Después de instalarlo no hay configuración adicional.

- Su configuración y declaración de tasks se realiza completamente en un fichero dentro del proyecto llamado "tasks.py".

- La documentación es amigable y extensa. Para usuarios poco familiarizados con el uso de Task runners, una buena [documentación](https://www.pyinvoke.org/) es esencial para comprender correctamente como usar dicho software, por lo que es un punto muy a su favor.

A nivel personal:

- Casi todos los desarrolladores (como en mi caso) están familiarizados con el uso de make, el cual puede ser utilizado como task runner. Invoke tiene una forma de uso muy similar a este, con la ventaja de ser específico para el lenguaje del proyecto (python) a la hora de escribir sus funciones, lo que me hace decantarme por su uso sin sentir que estoy utilizando una herramienta completamente desconocida, lo cual a nivel personal es de agradecer.

- Invoke, es una recomendación generalizada dentro de la comunidad de python en lo que a Task Runners se refiere.

- Cuenta con una gran comunidad siendo no solo la recomendación actual como se menciona previamente, si no también el que más personas tiene apoyando el proyecto a nivel de desarrollo, con mayor numero de PRs, watchers y estrellas.

Por todo lo mencionado previamente, creo que Invoke se adapta a los criterios establecidos y por lo tanto me he decantado por su uso en este proyecto como Task Runner.
  
# Gestión de dependencias
  
El proyecto utiliza [poetry](https://python-poetry.org/docs/) para gestionar las dependencias del mismo. Se trata de un software escrito en python que permite la gestión de dependencias y paquetes del lenguaje de manera cómoda y eficaz, encargandose de su instalanción y actualización. Para poder manejar dichas dependencias, se hace uso del archivo pyproject.toml donde se especifican. También aporta la posibilidad de crear entornos de desarrollo con las distintas versiones del software que estemos utilizando y nos permite lanzar ordenes dentro de los mismos.
 
