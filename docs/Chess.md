# Documentación sobre la toma de decisiones

## Planteamiento
Comenzamos por analizar las historias de usuario, principalmente [HU01](https://github.com/xCyal/A-Tracker/issues/3).

Nos encontramos con un usuario que decide utilizar nuestra aplicación para valorar una jugada de ajedrez en concreto, por lo que exporta su partida, o coloca la jugada en A-Tracker para obtener dicha valoración.

Lo que  como desarrolladores podemos deducir de dicha historia, son tres issues que debemos resolver:

- Claramente definido,el problema asociado a la valoración de la jugada, de este surge el issue [26](https://github.com/xCyal/A-Tracker/issues/26).

Para poder realizar dicha valoración, tenemos que ser capaces de representar la jugada. Para ello determinamos que los elementos que componen el ajedrez son:

- El tablero, el espacio sobre el que se colocan las piezas. ([Issue #17](https://github.com/xCyal/A-Tracker/issues/17))

- Las piezas, blancas y negras, peones, caballos, alfiles, torres, reyes y damas. ([Issue #44](https://github.com/xCyal/A-Tracker/issues/44))

Estos dos problemas, se pueden abordar de diferentes maneras. Podemos aproximarnos desde un punto de vista "Piece centric", o uno "Square centric".

## Aproximanción a la representación del ajedrez

Nos encontramos ante la decisión de como representar la jugada en concreto, y posteriormente, como representar la partida en conjunto. 

Lo primero que debemos de entender, es que **no estamos programando un juego de ajedrez**, si no una aplicación donde se puedan analizar las partidas o posiciones puntuales jugadas en otros soportes, para su estudio, a nivel de usuario (obtener un perfil de juego del usuario, encontrar errores repetitivos, estadísticas propias, comparar el juego con el de un rival...), como a nivel de juego (aquí entra la diferencia de material, valoración de jugadas...), con el fin de mejorar el juego del usuario, y generar un beneficio para este.

Partiendo de esta base, comenzamos a considerar las diferentes [aproximaciones posibles](https://www.chessprogramming.org/Board_Representation).

La aproximación de representar todo el tablero en base a las piezas, implica guardar de cada pieza, todos sus atributos (tipo, color), además de la posición en la que se encuentra, y las jugadas que puede realizar. Este modelo tiene un problema asociado, que los modelos "Square céntricos" no tienen, y es que es mucho más costoso el analisis del tablero en la posición que se encuentre, así como las jugadas posteriores.

En cuanto a la aproximación "Square céntrica", una de ellas sería una lista de casillas, que es la aproximación que se ha tomado para este proyecto, donde almacenamos en una matriz 8x8 (o vector de 64 casillas en este caso), que pieza, o en su defecto casilla vacía, se encuentra en esa posición.

Cabe mencionar, que para delimitar el tablero y evitar problemas a la hora de obtener los movimientos legales en esta aproximación al problema, se pueden implementar matrices mayores, con un delimitador de los bordes del tablero, pero dado que no estamos haciendo un juego, **si un movimiento es válido o no, es irrelevante** para la representación. Debido a esto, para almacenar las posiciones dentro de la clase Tablero, definida en el [issue #17](https://github.com/xCyal/A-Tracker/issues/16), se utilizará un vector de 64 casillas.

### Inicialización de Tablero

Es razonable pensar que este tablero se puede inicializar a la posición inicial convencional de una partida de ajedrez, pero A-Tracker pretende ser capaz de trabajar sobre [las diferentes modalidades de ajedrez](https://es.wikipedia.org/wiki/Variante_del_ajedrez) que se encuadren en un tablero cuadrado 8x8 convencional, así como quizás analizar solo jugadas concretas, cuya posición de partida puede ser un "tablero" diferente al primero, por lo que la inicialización debe de obtenerse de la propia información que se proporciona sobre la partida.

Las únicas limitaciones de inicialización de dicho tablero, será el tamaño del mismo, siendo siempre de 64 casillas, así como que las casillas sean del tipo adecuado.

Además se debe añadir un atributo que indique a que color le toca mover, siendo 0 negro y 1 blanco.

### Representación de las piezas

Deriva de la forma de representar que se ha elegido, la necesidad de decidir como representar las piezas.

Se podría utilizar, un int que represente el tipo de pieza(|1| ➡️ peón, |2| ➡️ alfíl...), positivo para blancas, negativo para negras y 0 en caso de estar vacía.

Otra posible aproximación, sería representar todas las piezas, y el color al que pertenecen, en un enumerado, con el añadido adicional de la casilla vacía. Esta representación trae problemas a la hora de operar con las piezas, ya que debemos de realizar siempre el doble de trabajo en cualquier algoritmo que use dichas piezas.

Es por esto que la representación final, se va a realizar con una clase Pieza. Dicha clase, tendrá dos atributos que representarán dicha pieza, el color, 0 negro o 1 blanco, y el tipo de pieza.

Por lo tanto los atributos de dicha clase serán _tipo_, que requiere del uso de un enum que se creará con los diferentes tipos de piezas (TipoPieza), y _blanco_ que determinará el color, siendo True si la pieza es blanca, y False si es negra.




