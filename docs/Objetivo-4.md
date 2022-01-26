# Información sobre el Objetivo 4

## Test Runner : Pytest

Se ha realizado una busqueda para obtener información sobre la actualidad de Test Runners/Test Frameworks en python.

Los criterios de búsqueda han sido el lenguaje (Python), su popularidad, sintaxis de las funciones y salida devuelta.

He encontrado resultados principalmente de [Pytest](https://docs.pytest.org/en/6.2.x/), [Robot](https://robotframework.org/), [Nose2](https://docs.nose2.io/en/latest/) y [Ward](https://ward.readthedocs.io/en/latest/).

Voy a mencionar algunas características que han influenciado el descarte de alguno de los mencionados:

- Nose2:
  - La salida no es muy descriptiva
  - El proyecto no se actualiza con tanta frecuencia como Pytest (menor comunidad, su propia página web te recomienda el uso de Pytest).

- Robot:
  - Sintaxis más compleja.
  - Buena comunidad, aunque no es la recomendación general
  - Requiere librerías externas 
  
- Ward:
  - Salida clara y descriptiva
  - Buen ritmo de desarrollo
  - Funcionalidades similares a pytest (Fixtures, parametrización de tests, uso de decoradores...)
  - Comunidad pequeña, Pytest es el indiscutible estandar.

Mi elección se ha visto influenciada por los motivos mencionados previamente, pero es necesario mencionar que el motivo con mayor peso es el hecho de que sea
el recomendado y más extendido en la propia comunidad de Python, lo que da cierta seguridad ya que usuarios más experimentados avalan su uso.
Obviamente este no es el único motivo, ya que estamos hablando de un Test Runner y en este caso la salida tras realizar los tests me parece también
un plus a favor de Pytest.

Por todo esto el Test Runner utilizado ha sido: Pytest.

## Biblioteca de aserciones: Assertpy

Se ha realizado una búsqueda para obtener información sobre la actualidad de bibliotecas de aserciones en python.

Los criterios de búsqueda han sido el lenguaje (Python), su popularidad, sintaxis de las aserciones y salida devuelta.

He encuntrado resultados principalmente de [Grappa](https://grappa.readthedocs.io/en/latest/), [Verify](https://github.com/dgilland/verify), [Assertpy](https://assertpy.github.io/docs.html) y [Unittest](https://docs.python.org/3/library/unittest.html) (como biblioteca de aserciones)

De entre ellas, mi elección se ha decantado entre Grappa y Assertpy, descartando el resto pues estas dos me parecen tener la sintaxis más sencilla, además de una popularidad bastante amplia.

- Assertpy y Grappa tienen ambas una sintaxis que se acerca mucho al lenguaje natural. En este caso, mi preferencia personal es la sintaxis de Assertpy.
- De entre las dos, la más recomendada por la comunidad es Assertpy, siendo esta además la más extendida.
- Assertpy es recomendada por el Test Runner elegido para este proyecto (Pytest)
- Grappa permite mostrar el código en caso de error, pero en este caso, esto ya podemos hacerlo con Pytest.
- Grappa permite lanzar excepciones.
- El proyecto de Assertpy está mucho más desarrollado, Grappa esta todavía en una etapa temprana de desarrollo.
- Assertpy ofrece un mayor rango de aserciones, lo cual probablemente no sea importante en este proyecto, pero si a una mayor escala.

En general, existen varias opciones válidas, pero a mi criterio personal uno de los motivos más importantes a la hora de elegir la biblioteca de aserciones,
es la sintaxis de la misma. Por esto mi decisión se decanto por Assertpy, ya que a preferencia personal tiene una sintaxis más amigable. Además, algunas razones
para elegir Grappa como sería el mostrar el código ya la obtenemos de nuestro Test Runner. Por esto y por el hecho de que Assertpy es la más extendida y por tanto 
la recomendación de la comunidad, así como de la otra herramienta añadida en este objetivo (Pytest), he optado por la opción segura y más establecida, Assertpy.

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


## Principios F.I.R.S.T

Se trata de los principios que se deben de seguir a la hora de crear pruebas unitarias.

- (F)ast: Las pruebas realizadas deben ser rápidas.
- (I)ndependent : Las pruebas deben ser independientes unas de otras y de su contexto.
- (R)epeatable : Repetibles, pudiendo ser lanzadas cuantas veces sean necesarias.
- (S)elf validating : Auto-Evaluación, es decir, la propia prueba determina el exito o el fracaso de la misma, no necesita una interpretación externa.
- (T)horought/(T)imely : Los tests deben de tener en cuenta las diferentes situaciones posibles / Los tests deben de ser creados antes que el código que van a testear, el código viene dado por los propios tests.

En nuestro proyecto se ha seguido los principios:
- Se tratan de unos tests rápidos, no tienen una gran carga computacional, también es debido a la escala del proyecto (apenas 0,1s).
- Ninguno de los tests requiere que otro test devuelva un resultado en concreto, son completamente independientes unos de otros, por lo que se podrían correr individualmente.
- Son repetibles ya que no dependen en ningún momento de factores externos como podría ser la máquina donde se este lanzando, una base de datos... Solo dependen de la propia clase (Tablero en este caso) que estan testando.
- En ningún momento es necesario una validación por parte de nadie para saber si el test ha pasado o ha fallado. Es el propio test el que determina esta situación, por lo que se cumple la "Auto-evaluación".
- Por último, los tests tienen en cuenta todos los posibles estados a la hora de crear los objetos que se estan testeando, además de que dicho código se ha creado posteriormente a los tests. Dichos tests vienen determinados por la [HU01](https://github.com/xCyal/A-Tracker/issues/3) de la cual hemos obtenido los tests o necesidades que debe cumplir el código que se implemente posteriormente, como en este caso el diseño de la clase o su método de puntuación.
