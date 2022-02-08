from enum import Enum

class TipoPieza(Enum):
  '''
     Enumerado encargado de indicar el nombre de cada pieza o posicion vacía en un tablero
  '''
  PEON = 1
  ALFIL = 2
  CABALLO = 3
  TORRE = 4
  DAMA = 5
  REY = 6
