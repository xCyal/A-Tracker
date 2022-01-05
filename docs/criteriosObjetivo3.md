# Criterios de uso de poetry como gestor de dependencias

Se ha elegido Poetry frente a otros como pip, pipenv o npm.

La documentación de Poetry es bastante clara y amigable para usuarios poco experimentados en su uso. Poetry nos permite su completo manejor desde un único archivo llamado pyproject.toml, cuya sintaxis es fácil de entender y manejar. Además los tiempos que toma son bastante menores que los anteriores a la hora de resolver las dependencias, cosa que en un entorno como el de nuestro proyecto, de pequeño tamaño, puede no ser notable, pero en caso de tener una gran de dependencias puede significar una ganancia significativa de tiempo.

En general poetry ha resultado a mi parecer una mejor opción, basandome no solo en los datos encontrados si no tambien en opiniones y críticas de usuarios que actualmente estan desarrollando proyectos en python de una escala mayor, que concuerdan con la facilidad de uso y ventajas de dicha herramienta.

# Criterios de uso de Invoke como Task runner

Se trata de un task runner especificamente utilizado para python, que en muchos sentidos tiene una forma de uso similar a Make con el cual la mayoría de desarrolladores estan familiarizados. Además, cuenta con una buena documentación lo que nos permite adaptarnos y implementar las tareas necesarias de manera rápida y eficaz.


# Sobre pylint

Pylint es un linter de python, es decir, software encargado de analizar el código fuente en busca de errores, existiendo una distinción clara entre los linters que solo buscan errores lógicos y los que buscan errores de estilo o sintaxis. De entre los que analizan tanto la parte lógica como la sintaxis, hemos elegido pylint por ser uno de los estándares actualmente, junto otros como flake8. 

Entre las caracteristicas que me han hecho decantarme por pylint, se encuentran algunas como el hecho de que es más riguroso con las "naming conventions" y porque en general se acepta pylint como una herramienta que realiza un analisis más detallado del código que otras, dando así una mayor variedad de opciones a la hora de realizar los checks.
