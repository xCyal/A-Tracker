import sys
sys.path.append("./")
sys.path.append("./tracker")

import pytest
from assertpy import assert_that

from tracker.tipo_pieza import *
from tracker.pieza import *
from tracker.tablero import *


peon_negro = Pieza(TipoPieza.PEON,False)

piezas_validas = [peon_negro] * 64   
piezas_invalidas = [peon_negro] * 63

tablero_valido = Tablero(piezas_validas)

def test_pieza_invalida():
    '''
    Test que el constructor de Pieza genera una excepcion si el tipo es invalido
    '''
    with pytest.raises(ValueError):
        Pieza("Peon",True)

def test_pieza_valida_tipo():
    '''
    Test encargado de comprobar que el constructor de pieza crea los objetos correctamente, en este caso comprobando su tipo
    '''
    assert_that(peon_negro.tipo).is_equal_to(TipoPieza.PEON)

def test_pieza_valida_blanco():
    '''
    Test encargado de comprobar que el constructor de pieza crea los objetos correctamente, en este caso comprobando su atributo "blanco"
    '''
    assert_that(peon_negro.blanco).is_equal_to(False)

def test_tablero_invalido():
    '''
    Test que el constructor de Tablero genera una excepcion si el tablero es invalido
    '''
    with pytest.raises(ValueError):
        Tablero(piezas_invalidas)


def test_tablero_valido_longitud():
    '''
    Test encargado de comprobar que el constructor crea los objetos correctamente, en este caso comprobando su longitud
    '''
    assert_that(tablero_valido.posicion_unica).is_length(64)

def test_tablero_valido_tipo():
    '''
    Test encargado de comprobar que el constructor crea los objetos correctamente, en este caso comprobando su tipo
    '''
    assert_that(tablero_valido.posicion_unica).contains_only(peon_negro)

def test_puntuacion_tablero():
    '''
    Test encargado de comprobar que el método de la clase Tablero "puntuacion_tablero" devuelve el resultado correcto.
    En este este caso el tablero de prueba tiene 64 peones negros, lo que implica una puntuación esperada de -64
    '''
    assert_that(tablero_valido.puntuacion_tablero()).is_equal_to(-64)
