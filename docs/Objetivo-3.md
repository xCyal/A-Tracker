# Elección de task runner:
## Invoke

Invoke es un "task execution tool & library", es decir, un software escrito en python que nos permite automatizar tareas sobre nuestros proyectos. Para ello utiliza un archivo llamado tasks.py sobre el cual se escriben las funciones deseadas (en el caso de este proyecto la función check, encargada de comprobar que el código de tracker compila), para más tarde poder invocar dichas funciones mediante el comando : - inv -funcion-

La razón del uso de invoke en nuestro proyecto viene dada por los siguientes motivos:

- Se trata de un Task runner específico para python. Esto significa que las funciones se escriben en un **estilo python**.

- La documentación es amigable y extensa. Para usuarios poco familiarizados con el uso de Task runners, una buena [documentación](https://www.pyinvoke.org/) es esencial para comprender correctamente como usar dicho software, por lo que es un punto muy a su favor.

- Casi todos los desarrolladores (como en mi caso) están familiarizados con el uso de make, el cual puede ser utilizado como task runner genérico. Invoke tiene una forma de uso muy similar a este, con la ventaja de ser específico para el lenguaje del proyecto (python) a la hora de escribir sus funciones, lo que me hace decantarme por su uso sin sentir que estoy utilizando una herramienta completamente desconocida.

- Invoke, es una recomendación generalizada dentro de la comunidad de python en lo que a Task runners se refiere. Se podría haber utilizado el propio Poetry, que ya se incluye en el proyecto, como Task runner, pero el uso de este último esta más enfocado a la gestión de dependencias y paquetes.

En general, es una opción de uso sencillo y que se adapta a las necesidades de este proyecto.
  
# Gestión de dependencias
  
El proyecto utiliza [poetry](https://python-poetry.org/docs/) para gestionar las dependencias del mismo. Se trata de un software escrito en python que permite la gestión de dependencias y paquetes del lenguaje de manera cómoda y eficaz, encargandose de su instalanción y actualización. Para poder manejar dichas dependencias, se hace uso del archivo pyproject.toml donde se especifican. También aporta la posibilidad de crear entornos de desarrollo con las distintas versiones del software que estemos utilizando y nos permite lanzar ordenes dentro de los mismos.
 
