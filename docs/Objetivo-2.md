# Documentación objetivo 2

Se ha creado la clase tablero y el enum pieza, ambas enfocadas al desarrollo de la [HU01](https://github.com/xCyal/A-Tracker/issues/3).
En esta historia de usuario se habla de un usuario, no profesional que desea conocer sus errores frecuentes a la hora de jugar al ajedrez.
De esta historia de usuario podemos obtener el issue central de este objetivo, el issue [#16](https://github.com/xCyal/A-Tracker/issues/16).

El issue [#16](https://github.com/xCyal/A-Tracker/issues/16) nos plantea el problema de diseñar una clase que pueda determinar la posición de un tablero de ajedrez en un momento dado,
para más tarde poder utilizar esta clase a la hora de llevar el seguimiento de una partida, sobre la que se realizará el analisis y por lo tanto la busqueda de errores de nuestro usuario en [#16](https://github.com/xCyal/A-Tracker/issues/16).

Respecto a la forma de desarrollarlo, hemos creado un enum que nos permita determinar que tipo de pieza se encuentra en una casilla en concreto, para más tarde en la clase tablero, crear las casillas (64) y que se determine la posición en las que estan.
