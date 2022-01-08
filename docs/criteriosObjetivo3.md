# Poetry como gestor de dependencias

Se ha elegido Poetry como gestor de dependencias para este proyecto frente a otros como pip o pipenv.

He utilizado pip en otras ocasiones, y me he decantado por utilizar poetry por su facilidad a la hora de administrarlo, ya que requiere algo más de tiempo para su correcta configuración y uso.

Respecto a pipenv, nunca lo he utilizado personalmente, pero parece ser una buena alternativa a poetry y bastante aceptada en la comunidad de python, quizas siendo su documentación algo menos clara que la de poetry para mi gusto personal.

La documentación de Poetry es bastante clara y amigable para usuarios poco experimentados en su uso. Poetry nos permite su completo manejor desde un único archivo llamado pyproject.toml, cuya sintaxis es fácil de entender y manejar.

En general poetry ha resultado a mi parecer una mejor opción, basandome no solo en los datos encontrados si no tambien en opiniones y críticas de usuarios que actualmente estan desarrollando proyectos en python de una escala mayor, que concuerdan con la facilidad de uso y ventajas de dicha herramienta.

# Criterios de uso de Invoke como Task runner

Se trata de un task runner especificamente utilizado para python, que en muchos sentidos tiene una forma de uso similar a Make con el cual la mayoría de desarrolladores estan familiarizados. Además, cuenta con una buena documentación lo que nos permite adaptarnos y implementar las tareas necesarias de manera rápida y eficaz.

Entre los motivos por los que he elegido utilizar invoke, se encuentra el hecho de salir de la zona de confort ya que make es una herramienta que he utilizado ampliamente durante toda mi expericencia académica, y considero invoke una buena opción por lo previamente mencionado de su parecido en cuestiones de similaridad en su uso respecto a make, sin ser make, además de ser de uso común entre la comunidad de python.

# Sobre pylint

La función de check, cuyo proposito en este objetivo era comprobar que los archivos compilaban, no necesitaba del uso de pylint, pero se ha añadido para además comprobar la sintaxis de dichos archivos. Podríamos haber simplemente realizado alguna orden de python como "python -m py_compile DIR" y comprobar la existencia de errores.

Pylint es un linter de python, es decir, software encargado de analizar el código fuente en busca de errores, existiendo una distinción clara entre los linters que solo buscan errores lógicos y los que buscan errores de estilo o sintaxis. De entre los que analizan tanto la parte lógica como la sintaxis, hemos elegido pylint por ser uno de los estándares actualmente, junto otros como flake8. 

Entre las caracteristicas que me han hecho decantarme por pylint, se encuentran algunas como el hecho de que es más riguroso con las "naming conventions" y porque en general se acepta pylint como una herramienta que realiza un analisis más detallado del código que otras, dando así una mayor variedad de opciones a la hora de realizar los checks.
