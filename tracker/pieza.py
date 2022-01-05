from enum import Enum

class Pieza(Enum):
  '''
     Enumerado encargado de indicar el nombre de cada pieza o posicion vacía en un tablero
  '''
  REY_BLANCO = 1
  REY_NEGRO = 2
  REINA_BLANCO = 3
  REINA_NEGRO = 4
  ALFIL_BLANCO = 5
  ALFIL_NEGRO = 6
  TORRE_BLANCO = 7
  TORRE_NEGRO = 8
  CABALLO_BLANCO = 9
  CABALLO_NEGRO = 10
  PEON_BLANCO = 11 
  PEON_NEGRO = 12
  EMPTY = 13