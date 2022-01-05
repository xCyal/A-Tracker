# Criterios de uso de poetry como gestor de dependencias

Se ha elegido Poetry frente a pip tras algo de investigación debido a que su eficiencia respecto a este último es mayor, dando una mejor performance. Además, es mucho más sencillo en su instalación y manejo, permitiendonos manejarle casi completamente desde un solo archivo "pyproject.toml" 

La documentación de Poetry es bastante clara y amigable para usuarios poco experimentados en su uso, otro de los motivos de peso para su elección. 

# Criterios de uso de Invoke como Task runner

Se trata de un task runner especificamente utilizado para python, que en muchos sentidos tiene una forma de uso similar a Make con el cual la mayoría de desarrolladores estan familiarizados. Además, cuenta con una buena documentación lo que nos permite adaptarnos y implementar las tareas necesarias de manera rápida y eficaz.


# Sobre pylint

Pylint es un linter de python, es decir, software encargado de analizar el código fuente en busca de errores, existiendo una distinción clara entre los linters que solo buscan errores lógicos y los que buscan errores de estilo o sintaxis. De entre los que analizan tanto la parte lógica como la sintaxis, hemos elegido pylint por ser uno de los estándares actualmente, junto otros como flake8. 

Entre las caracteristicas que me han hecho decantarme por pylint, se encuentran algunas como el hecho de que es más riguroso con las "naming conventions" y porque en general se acepta pylint como una herramienta que realiza un analisis más detallado del código que otras, dando así una mayor variedad de opciones a la hora de realizar los checks.
