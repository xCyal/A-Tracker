# Elección de task runner:
## Invoke

Invoke es un "task execution tool & library", es decir, un software escrito en python que nos permite automatizar tareas sobre nuestros proyectos. Para ello utiliza un archivo llamado tasks.py sobre el cual se escriben las funciones deseadas (en el caso de este proyecto la función check, encargada de comprobar que el código de tracker compila), para más tarde poder invocar dichas funciones mediante el comando : - inv -funcion-

La razón del uso de invoke en nuestro proyecto viene dada por los siguientes motivos:

- La documentación es amigable y extensa. Para usuarios poco familiarizados con el uso de Task runners, una buena [documentación](https://www.pyinvoke.org/) es esencial para comprender correctamente como usar dicho software, por lo que es un punto muy a su favor.

- Casi todos los desarrolladores (como en mi caso) están familiarizados con el uso de make, el cual puede ser utilizado como task runner genérico. Invoke tiene una forma de uso muy similar a este, con la ventaja de ser específico para el lenguaje del proyecto (python) a la hora de escribir sus funciones, lo que me hace decantarme por su uso sin sentir que estoy utilizando una herramienta completamente desconocida, lo cual a nivel personal es de agradecer.

- Invoke, es una recomendación generalizada dentro de la comunidad de python en lo que a Task runners se refiere.

- Cuenta con una gran comunidad siendo no solo la recomendación actual como se menciona previamente, si no también el que más personas tiene apoyando el proyecto a nivel de desarrollo, con mayor numero de PRs, watchers y estrellas.

- No tiene dependencias adicionales.

- Su configuración y declaración de tasks se realiza completamente en un fichero dentro del proyecto llamado "tasks.py".

- Específico para el lenguaje del proyecto (Python).

### Algunas características de otros task runners que he revisado para realizar la elección: 

- [Make](https://www.gnu.org/software/make/manual/make.html) (Puede servir como Task runner, aunque su principal uso no es como tal, puede ser una buena opción):
  - Manejo desde un solo archivo Makefile.
  - No es específico de python. *
  - Sintaxis sencilla.

- [Doit](https://pydoit.org/contents.html):
  - Específico para python
  - Incluye dependencias externas *
  - Configuración en un fichero 

- [Poethepoet](https://github.com/nat-n/poethepoet):
  - Específico para python
  - Incluye dependencias externas *
  - Configuración algo más complicada que el resto *
  - Configuración en pyproject.toml 

Estos son los más extendidos a parte de invoke, he de mencionar que he encontrado otros como [Pypyr](https://pypyr.io/docs/) o [Taskipy](https://github.com/illBeRoy/taskipy), los cuales no parecen tener carácteristicas novedosas respecto a los anteriores además de encontrar bastante menos documentación sobre ellos.

Respecto a los aquí mencionados, la elección de invoke viene principalmente por los puntos marcados, o bien tienen dependencias externas, no son específicos para python, o su configuración puede no ser tan sencilla como en Invoke e incluso en casos como Taskipy o Poethepoet depender directamente de pyproject.toml. Además las comunidades que respaldan a estos Task runners son considerablemente menores y su uso mucho menos extendido que el de Invoke.

  
# Gestión de dependencias
  
El proyecto utiliza [poetry](https://python-poetry.org/docs/) para gestionar las dependencias del mismo. Se trata de un software escrito en python que permite la gestión de dependencias y paquetes del lenguaje de manera cómoda y eficaz, encargandose de su instalanción y actualización. Para poder manejar dichas dependencias, se hace uso del archivo pyproject.toml donde se especifican. También aporta la posibilidad de crear entornos de desarrollo con las distintas versiones del software que estemos utilizando y nos permite lanzar ordenes dentro de los mismos.
 
