# Documentación objetivo 2

En la [HU01](https://github.com/xCyal/A-Tracker/issues/3), un usuario, habla de que le gustaría tener la posibilidad de obtener una valoración sobre un movimiento que ha realizado, para saber si es bueno o malo, a partir de como se encuentran las piezas en un momento dado. Si subdividimos esta historia, llegamos al a conclusión de que necesitamos una forma de almacenar una posición de las piezas, es decir, un tablero Issue [#16](https://github.com/xCyal/A-Tracker/issues/16). 

Adicionalmente, necesitamos una forma de deducir si esta posición, se trata de una posición favorable o desfavorable, ya que es lo que el usuario necesita. De esta situación, surge el issue [#26](https://github.com/xCyal/A-Tracker/issues/26), donde se aplica [la teoría del valor relativo de las piezas](https://es.wikipedia.org/wiki/Valor_relativo_de_las_piezas_de_ajedrez), para deducir, de forma básica, si se encuentra en una posición ventajosa para blancas, para negras, o en un empate de material.

Es de estos dos issues, [#26](https://github.com/xCyal/A-Tracker/issues/26) y [#16](https://github.com/xCyal/A-Tracker/issues/16), de donde se extrae la clase tablero, y la funcionalidad asociada de obtener una puntuación sobre esta clase.
