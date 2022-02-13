# :chart_with_downwards_trend: A-tracker :chart_with_upwards_trend:

- Un proyecto para la asignatura IV -

## Motivación de A-Tracker 	:man_student::woman_student:

Durante años los usuarios de (video)juegos de todo el mundo han intentado encontrar en su manera de actuar, errores recurrentes y fallos que les permitan mejorar su puntuación en el ranking ⚔️

Existen numerosas asociaciones y escuelas enfocadas en el aprendizaje de juegos de estrategia, que en ocasiones se encuentran al alcance de pocas personas, ya sea por motivos como el precio de las mismas o el hecho de que gran mayoría de los jugadores no son profesionales ni pretenden dedicar una gran cantidad de tiempo al estudio de su juego, lo cual no implica que una aplicación que les ayudara en sus ratos libres a mejorar no fuera una buena opción para ellos.


## Objetivo de A-Tracker :dart:

A-Tracker se creará con la intención de proporcionar al usuario una herramienta encargada de generar un perfíl de juego propio de cada uno de sus usuarios, permitiendo visualizar de manera clara los errores cometidos al generar estadísticas y comparaciones con otros perfiles de usuarios que tengan una mejor performance, de manera que se pueda extraer los puntos clave donde los jugadores deben mejorar y realizar un análisis de como hacerlo, en base a lo aprendido de jugadores mejores o de la comunidad al completo.

De esta forma A-Tracker sera una buena opción para personas que deseen dedicarle un tiempo limitado a mejorar, así como para personas que tengan un conocimiento alto y necesiten un buen soporte que realize un analisis sobre el propio usuario o sus rivales.



# Documentación Objetivo 1

Puedes encontrar más información sobre el proyecto en [/docs](/docs).

- [generalJourney.md](/docs/generalJourney.md)

# Documentación Objetivo 2

Puedes encontrar más información del objetivo 2 en la [documentacion asociada](/docs/Objetivo-2.md)

# Documentación Objetivo 3

Puedes encontrar más información del objetivo 3 en la [documentación asociada](/docs/Objetivo-3.md)

Para instalar poetry podemos encontrar las instrucciones en su [documentación](https://python-poetry.org/docs/)

Para el correcto funcionamiento de este objetivo debes de tener instaladas las dependencias, para ello utilizamos el gestor de dependencias (Poetry) desde el directorio del proyecto:

- 'poetry install'

Una vez se ha instalado las dependencias podemos proceder a utilizar el siguiente comando para checkear la sintaxis de los archivos .py de nuestro proyecto:

- 'inv check'

# Documentación Objetivo 4

Puedes encontrar más información del objetivo 4 en la [documentación asociada](/docs/Objetivo-4.md)

Para el correcto funcionamiento de este objetivo debes de tener instaladas las dependencias, para ello utilizamos el gestor de dependencias (Poetry) desde el directorio del proyecto:

- 'poetry install'

Después para acceder al entorno creado por poetry:

- 'poetry shell'

Podemos lanzar los tests con nuestro gestor de tareas:

- 'inv test'

# Documentación Objetivo 5

Puedes encontrar más información del objetivo 5 en la [documentación asociada](/docs/Objetivo-5.md)

Existen dos opciones para lanzar los tests en el contenedor de pruebas:

Crear el contenedor con:

- 'inv dbuild'

y después lanzar los tests dentro de el con:

- 'inv drun'

La otra opción es acceder al contenedor [aquí](https://hub.docker.com/repository/docker/xcyal/tracker).
