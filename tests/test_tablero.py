import sys

sys.path.append('./')
sys.path.append('../tracker/')

from tracker.tablero import Tablero
from tracker.pieza import Pieza
import pytest
from assertpy import assert_that

lista_valida = [Pieza.TORRE_NEGRO,Pieza.CABALLO_NEGRO,Pieza.ALFIL_NEGRO,Pieza.REINA_NEGRO,Pieza.REY_NEGRO,Pieza.ALFIL_NEGRO,Pieza.CABALLO_NEGRO,Pieza.TORRE_NEGRO,
Pieza.PEON_NEGRO,Pieza.PEON_NEGRO,Pieza.PEON_NEGRO,Pieza.PEON_NEGRO,Pieza.PEON_NEGRO,Pieza.PEON_NEGRO,Pieza.PEON_NEGRO,Pieza.PEON_NEGRO,
Pieza.EMPTY,Pieza.EMPTY,Pieza.EMPTY,Pieza.EMPTY,Pieza.EMPTY,Pieza.EMPTY,Pieza.EMPTY,Pieza.EMPTY,
Pieza.EMPTY,Pieza.EMPTY,Pieza.EMPTY,Pieza.EMPTY,Pieza.EMPTY,Pieza.EMPTY,Pieza.EMPTY,Pieza.EMPTY,
Pieza.EMPTY,Pieza.EMPTY,Pieza.EMPTY,Pieza.EMPTY,Pieza.EMPTY,Pieza.EMPTY,Pieza.EMPTY,Pieza.EMPTY,
Pieza.EMPTY,Pieza.EMPTY,Pieza.EMPTY,Pieza.EMPTY,Pieza.EMPTY,Pieza.EMPTY,Pieza.EMPTY,Pieza.EMPTY,
Pieza.PEON_BLANCO,Pieza.PEON_BLANCO,Pieza.PEON_BLANCO,Pieza.PEON_BLANCO,Pieza.PEON_BLANCO,Pieza.PEON_BLANCO,Pieza.PEON_BLANCO,Pieza.PEON_BLANCO,
Pieza.TORRE_BLANCO,Pieza.CABALLO_BLANCO,Pieza.ALFIL_BLANCO,Pieza.REINA_BLANCO,Pieza.REY_BLANCO,Pieza.ALFIL_BLANCO,Pieza.CABALLO_BLANCO,Pieza.TORRE_BLANCO]


lista_invalida = [Pieza.TORRE_NEGRO,Pieza.CABALLO_NEGRO,Pieza.ALFIL_NEGRO,Pieza.REINA_NEGRO,Pieza.REY_NEGRO,Pieza.CABALLO_NEGRO,Pieza.TORRE_NEGRO,
Pieza.PEON_NEGRO,Pieza.PEON_NEGRO,Pieza.PEON_NEGRO,Pieza.PEON_NEGRO,Pieza.PEON_NEGRO,Pieza.PEON_NEGRO,Pieza.PEON_NEGRO,Pieza.PEON_NEGRO,
Pieza.EMPTY,Pieza.EMPTY,Pieza.EMPTY,Pieza.EMPTY,Pieza.EMPTY,Pieza.EMPTY,Pieza.EMPTY,Pieza.EMPTY,
Pieza.EMPTY,Pieza.EMPTY,Pieza.EMPTY,Pieza.EMPTY,Pieza.EMPTY,Pieza.EMPTY,Pieza.EMPTY,
Pieza.EMPTY,Pieza.EMPTY,Pieza.EMPTY,Pieza.EMPTY,Pieza.EMPTY,Pieza.EMPTY,Pieza.EMPTY,
Pieza.EMPTY,Pieza.EMPTY,Pieza.EMPTY,Pieza.EMPTY,Pieza.EMPTY,Pieza.EMPTY,Pieza.EMPTY,Pieza.EMPTY,
Pieza.PEON_BLANCO,Pieza.PEON_BLANCO,Pieza.PEON_BLANCO,Pieza.PEON_BLANCO,Pieza.PEON_BLANCO,Pieza.PEON_BLANCO,Pieza.PEON_BLANCO,Pieza.PEON_BLANCO,
Pieza.TORRE_BLANCO,Pieza.CABALLO_BLANCO,Pieza.ALFIL_BLANCO,Pieza.REINA_BLANCO,Pieza.REY_BLANCO,Pieza.ALFIL_BLANCO,Pieza.CABALLO_BLANCO,Pieza.TORRE_BLANCO]


lista_puntuacion_diferente = [Pieza.TORRE_NEGRO,Pieza.CABALLO_NEGRO,Pieza.EMPTY,Pieza.REINA_NEGRO,Pieza.REY_NEGRO,Pieza.ALFIL_NEGRO,Pieza.CABALLO_NEGRO,Pieza.TORRE_NEGRO,
Pieza.PEON_NEGRO,Pieza.PEON_NEGRO,Pieza.PEON_NEGRO,Pieza.PEON_NEGRO,Pieza.PEON_NEGRO,Pieza.PEON_NEGRO,Pieza.PEON_NEGRO,Pieza.PEON_NEGRO,
Pieza.EMPTY,Pieza.EMPTY,Pieza.EMPTY,Pieza.EMPTY,Pieza.EMPTY,Pieza.EMPTY,Pieza.EMPTY,Pieza.EMPTY,
Pieza.EMPTY,Pieza.EMPTY,Pieza.EMPTY,Pieza.EMPTY,Pieza.EMPTY,Pieza.EMPTY,Pieza.EMPTY,Pieza.EMPTY,
Pieza.EMPTY,Pieza.EMPTY,Pieza.EMPTY,Pieza.EMPTY,Pieza.EMPTY,Pieza.EMPTY,Pieza.EMPTY,Pieza.EMPTY,
Pieza.EMPTY,Pieza.EMPTY,Pieza.EMPTY,Pieza.EMPTY,Pieza.EMPTY,Pieza.EMPTY,Pieza.EMPTY,Pieza.EMPTY,
Pieza.PEON_BLANCO,Pieza.PEON_BLANCO,Pieza.PEON_BLANCO,Pieza.PEON_BLANCO,Pieza.PEON_BLANCO,Pieza.PEON_BLANCO,Pieza.PEON_BLANCO,Pieza.PEON_BLANCO,
Pieza.TORRE_BLANCO,Pieza.CABALLO_BLANCO,Pieza.ALFIL_BLANCO,Pieza.REINA_BLANCO,Pieza.REY_BLANCO,Pieza.ALFIL_BLANCO,Pieza.CABALLO_BLANCO,Pieza.TORRE_BLANCO]

tablero_valido = Tablero(lista_valida)
tablero_invalido = Tablero(lista_invalida)
tablero_desbalanceado = Tablero(lista_puntuacion_diferente)

def test_posiciones_correctas():
   assert_that(tablero_valido._posicion).is_length(64)
   
def test_posiciones_incorrectas():
   assert_that(tablero_invalido._posicion).is_empty()

def test_puntuacion_balanceada():
   assert_that(tablero_valido.puntuar_tablero()).is_equal_to(0)

def test_puntuacion_desbalanceada():
   tablero_desbalanceado.puntuar_tablero()
   assert_that(tablero_desbalanceado.puntuar_tablero()).is_not_equal_to(0)
