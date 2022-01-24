# Información sobre el Objetivo 4

## Sobre los tests de la clase Tablero

La clase Tablero será la encargada de almacenar la información de un punto exacto de una partida de ajedrez,
con la idea de que se concatenen numerosos tableros para así obtener la partida completa. 

Teniendo esta idea de base, los tests se obtienen de las propias historias de usuario [HU01](https://github.com/xCyal/A-Tracker/issues/3).
En esta historia se observa un usuario que después de jugar varias partidas, quiere comprobar los errores cometidos.
Para ello debemos establecer un sistema de puntuación de una situación concreta de la partida para así poder observar donde se han cometido errores.
Esta sería la base de un futuro analisis más profundo. De aquí surge el [issue asociado](https://github.com/xCyal/A-Tracker/issues/26).
Una vez tenemos parte de la lógica de negocio implementada, es hora de comprobar el correcto funcionamiento de la clase Tablero encargada de estas funcionalidades.
Para ello hemos creado 4 tests diferentes, uno encargado de comprobar que el método de puntuación funciona correctamente, dos para ver sí un Tablero que supuestamente
debería inicializarse bien (longitud 64, tipo Pieza) da el resultado esperado, y un último para en caso en el que comprobamos si un Tablero que no debería de inicializarse
devuelve la excepción esperada.

Respecto a la inicialización del Tablero de ajedrez a una posición inicial, he de mencionar que no es necesario. A-Tracker no es un juego de ajedrez, obtiene información
de las partidas de ajedrez, pero en ningún momento necesita implementar un tablero desde el inicio o los diferentes movimientos de las piezas, solo una representación
de las mismas. Es por esto que los tableros de prueba se crean en el archivo de tests, dado que simulamos una situación realista.
