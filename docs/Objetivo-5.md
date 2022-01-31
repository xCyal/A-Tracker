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

## Posibles imagenes base

Se ha buscado información acerca de las posibilidades existentes en la actualidad para utilizar como imagen base de nuestro contenedor.

Se puede utilizar una imagen de un SO como ubuntu:20.04 como base, pero como se verá en las pruebas posteriores tiene demasiadas funcionalidades innecesarias para este proyecto, habíendo mejores opciones.

La primera imagen que he testeado es la oficial de python en Docker, basada en Debian 11. Contiene todo lo necesario para un proyecto en python (este caso versión 3.8) y no debería tener problemas de compatibilidad o falta de dependencias, así como ser estable.

De la imagen oficial de python en Docker (basada en Debian 11), encontramos una buena opción en una de sus variantes, python:3.8-slim, conteniendo esta solo los paquetes necesarios para utilizar python en esta distribución, de esta manera siendo menor que la base y construyendo los contenedores de manera mas rápida.

Por otra parte, otra imagen muy extendida es la de python:3-8-alpine, basada en alpine, de un tamaño muy pequeño, aunque hay que mencionar que puede causar problemas de compatibilidad, además de no contener algunos paquetes que podrían ser necesarios, dando lugar a menor estabilidad.

## Comparación entre imagenes

Vamos a hablar de el tamaño de dichas imagenes trás ser utilizadas como base de mi Dockerfile:

| Imagen           | Tamaño  | Pasa los tests | Build Time              |
| -----------------| --------|----------------|------------------------ |
| python:3.8 (base)| 939 MB  |  ✔️            | 46.736s                |
| python:3.8-slim  | 176 MB  |  ✔️            | 33.301s                |
| python:3.8-alpine| 196 MB  |  ✔️            | 45.222s                |
