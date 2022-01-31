# Información sobre el Objetivo 5

## Criterios de elección de la imagen base

Se ha realizado una busqueda para obtener información sobre las imagenes de python que podríamos tomar como base para nuestro contenedor y que se adapten mejor a las necesidades de nuestro proyecto.

Los requisitos para que una imagen sea una opción son los siguientes:

- Contener python o permitir su instalación, dado que este proyecto se esta llevando a cabo en python.

- Tener el menor tamaño posible, así como tiempo de construcción.

- Debe ser una imagen estable.

## Elección de la versión de python

Se va a utilizar una versión 3.8 de python. 

Existen versiones posteriores (3.9.x 3.10.0) las cuales se puede observar que se encuentran en estado de "bugfix".

Mencionaré que también se podría usar la 3.7 que se encuentra en el mismo estado que la 3.8 como podemos observar en la tabla, pero la 3.8 es mejor en este caso ya que la diferencia principal entre ellas son pequeños cambios en el comportamiento del lenguaje, algunos añadidos a la sintaxis del mismo, y mejoras en lo que a velocidad se refiere. 

Las anteriores versiones se consideran en estado "end-of-life" (EOL).

