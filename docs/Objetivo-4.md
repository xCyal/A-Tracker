# Información sobre el Objetivo 4

## Test Runner : Pytest

Se ha realizado una busqueda para obtener información sobre la actualidad de Test Runners/Test Frameworks en python.

Los criterios de búsqueda han sido el lenguaje (Python), su popularidad, sintaxis de las funciones y salida devuelta.

He encontrado resultados principalmente de [Pytest](https://docs.pytest.org/en/6.2.x/), [Robot](https://robotframework.org/), [Nose2](https://docs.nose2.io/en/latest/) y [Ward](https://ward.readthedocs.io/en/latest/).


Para este proyecto he utilizado Pytest. Desde un punto de vista personal he decidido usarlo, después de haber probado los otros aquí mencionados, ya que en general creo que cumple mejor con los critérios mencionados. Robot ha quedado descartado dado que la sintaxis para crear las funciones es más complicada de que la de Pytest o Ward, aunque me ha gustado la posibilidad de obtener el resultado de los test en XML si necesidad de ningún plugin como en Pytest. En el aspecto de la salida, Nose2 era el que menos me ha gustado, a esto le sumamos el hecho de que es un proyecto que tiene poca actividad en su desarrollo, por lo que he decidido no continuar utilizandolo. Existe un precedente a Nose2, Nose, el cual también he probado, pero este proyecto ya lleva abandonado más de 6 años, y no parece tener ninguna ventaja a priori respecto a Nose2 más alla de la posibilidad de usar bastantes más plugins de los existentes para Nose2, pero no me convence por los mismos motivos que Nose2 añadidos a su abandono. La salida de Pytest me parece la mejor de los que he probado, en este caso solo siendo comparable la de Ward, que también me pareció clara y sencilla de entender. Mi decisión final de descartar Ward, dado que para este proyecto tiene las funcionalidades necesarias y cumple con las expectativas (sintaxis sencilla, una muy buena salida, funcionalidades similares a Pytest), es principalmente el hecho de que Pytest esta avalado por una amplia cantidad de usuarios de Python, cuya experiencia hay que tener en cuenta, siendo este el más extendido en la comunidad y el que mejor valoración tiene. Desde mi punto de vista Ward es un proyecto a la altura de Pytest, ya que en muchos sentidos son similares, pero todavía le falta algo de visibilidad.

Conclusión: Como expliqué en la presentación y se menciona aquí, Ward me parece una opción a la altura de Pytest, y que la popularidad aunque se mencione  como criterio, siempre ha sido en última instancia, para en caso de "empate técnico" decidirme por una u otra. Quizás he optado por la opción más asentada para no encontrarme con problemas indocumentados o por falta de valor, pero recomiendo, y animo a cualquiera a utilizar Ward.


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

## Sobre los tests de la clase Tablero y Pieza

La clase Tablero será la encargada de almacenar la información de un punto exacto de una partida de ajedrez.

La clase Pieza será la encargada de representar las piezas dentro de este tablero.

Los tests que se han desarrollado se encargan de comprobar que los objetos de las clases Pieza y Tablero se crean correctamente, así como en caso de introducir parámetros indeseados, lanzan las excepciones correspondientes. Estos tests se extraen de los issues [#45](https://github.com/xCyal/A-Tracker/issues/45) y [#29](https://github.com/xCyal/A-Tracker/issues/45)

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
